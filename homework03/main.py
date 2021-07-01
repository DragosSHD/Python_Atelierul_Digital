from web_scrapper import *

print('Hi! Let\'s start web scrapping. Enter the category link below: ')
print('Example link: https://xtrems.ro/84-casti')
crt_url = input()
get_product_list(crt_url)
