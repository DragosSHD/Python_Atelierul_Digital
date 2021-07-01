import requests
from bs4 import BeautifulSoup
import json
from os import path


# Function that takes the information from the given page and returns a list containing a dictionary formatted
# according to the attributes received.
def prod_from_crt_page(page_url, attr):
    crt_list = []
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, features='html.parser')

    product_list = soup.find(id='js-product-list').find_all('div', class_='product_list_item')

    for crt_product in product_list:
        prod_name = prod_price = prod_size = 'Undefined'
        prod_stock = 'Out of Stock'
        if crt_product.find('h3', class_='s_title_block').find('a'):
            prod_name = crt_product.find('h3', class_='s_title_block').find('a').text
        if crt_product.find('span', class_='price'):
            prod_price = crt_product.find('span', class_='price').text.split()[0]
        if crt_product.find('span', class_='st_attr_list_text'):
            prod_size = [size.text for size in crt_product.find_all('span', class_='st_attr_list_text')]
        if crt_product.find('a', class_='ajax_add_to_cart_button'):
            prod_stock = 'In Stock'

        prod_attr = [prod_name, prod_price, prod_stock, prod_size]
        crt_list.append({col: data for col, data in zip(attr, prod_attr)})
    return crt_list


# Checks if the given page exists. If it encounters an empty page, it signals it so that the iteration through the
# pages of the current category can stop.
def check_if_exists(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, features='html.parser')

    empty_category = soup.find(id='js-product-list').find('article', class_='alert-warning')

    return False if empty_category else True


# Checks if a json file was already created for the given category.
def check_if_file_exists(file_name):
    if path.exists(file_name):
        print("The category has been previously scrapped so we will do the comparison with the last version.")
        return True
    print("The category is new, so we'll simply add it for future comparison.")
    return False


# Get a float from the price string.
def format_price(str_price):
    str_price = str_price.split('.')[0] + str_price.split('.')[1]  # remove the '.'
    str_price = str_price.split(',')[0] + '.' + str_price.split(',')[1]  # replace ',' with '.'
    return float(str_price)


def compare_product_prices(file_name, crt_array):
    prev_array = []
    differences_dict = {}
    count_diff = 0
    with open(file_name) as json_file:
        prev_array = json.load(json_file)

    for crt_prod_info in crt_array:
        for prev_prod_info in prev_array:
            if crt_prod_info['Product Name'] == prev_prod_info['Product Name']:
                if crt_prod_info['Price'] != prev_prod_info['Price']:
                    price_diff = abs(format_price(crt_prod_info['Price']) -
                                     format_price(prev_prod_info['Price']))
                    count_diff += 1
                    differences_dict[crt_prod_info['Product Name']] = price_diff
                    break
    if count_diff == 0:
        print('No difference has been found!')
    else:
        print('There are ' + str(count_diff) + ' differences for the products:\n')
    for key_name, value_price in differences_dict.items():
        print(key_name)
        print('With a price difference of: ' + str(value_price) + ' lei.\n')


def get_product_list(page_url):
    attributes = ['Product Name', 'Price', 'Stock', 'Available Sizes']
    xtremz_products = []
    crt_url = page_url + '?page=1'
    iterator = 1
    while check_if_exists(crt_url):
        xtremz_products += prod_from_crt_page(crt_url, attributes)
        iterator += 1
        crt_url = crt_url[:-1]
        crt_url += str(iterator)

    json_file_name = page_url.split('/')[-1] + '.json'

    if check_if_file_exists(json_file_name):
        compare_product_prices(json_file_name, xtremz_products)
        while True:
            decision = input('Would you like to overwrite the file? Y/N\n')
            if decision == 'Y':
                with open(json_file_name, mode='w') as json_file:
                    json.dump(xtremz_products, json_file, indent=2)
                print('Category info has been saved!')
                break
            elif decision == 'N':
                print('The file remains untouched.')
                break
            else:
                print('Wrong input.')
                continue
    else:
        with open(json_file_name, mode='w') as json_file:
            json.dump(xtremz_products, json_file, indent=2)
        print('Category info has been saved!')
