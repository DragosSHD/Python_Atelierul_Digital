import requests
from bs4 import BeautifulSoup
import json


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


def check_if_exists(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, features='html.parser')

    empty_category = soup.find(id='js-product-list').find('article', class_='alert-warning')

    return False if empty_category else True


def get_product_list(page_url):
    attributes = ['Product Name', 'Price', 'Stock', 'Available Sizes']
    xtremz_products = []
    page_url = 'https://xtrems.ro/577-casti-enduro-mx'
    crt_url = page_url + '?page=1'
    iterator = 1
    while check_if_exists(crt_url):
        xtremz_products += prod_from_crt_page(crt_url, attributes)
        iterator += 1
        crt_url = crt_url[:-1]
        crt_url += str(iterator)
        print(crt_url)

    with open('inventory.json', mode='a') as json_file:
        json.dump(xtremz_products, json_file, indent=2)




