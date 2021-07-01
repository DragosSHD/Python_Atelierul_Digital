# What we've done during the fourth python course.

# Memory Savers
# - lambda functions: used inline so we won't occupy memory with a function that we have to use only once
import json

my_sum = (lambda param1, param2: param1 + param2)(5, 7)
print('my_sum', my_sum)

# - map functions: receives a function and applies it on an iterable object in order to modify each of it's objects

numbers = (1, 2, 3, 4, 5)
numbers_modified = list(map(lambda nr: nr * 2, numbers))

print('numbers', numbers)
print('numbers', numbers_modified)

# - filter: receives a function returning a boolean so we can filter an iterable based on the actions defined within the
#           given function.

print('filtered numbers:', list(filter(lambda nr: nr > 3, numbers)))

# - zip: returns a zip object which adds objects from the given lists in "baskets"

zip_object = zip([10, 20, 30, 40, 50], (1, 2, 3, 4, 5), (6, 7, 8, 9, 10))
print('zip_object', list(zip_object))

# - map and filter functions can be easily replaced through comprehension. (list comprehension)

dict_keys = ('a', 'b', 'c')
numbers = (1, 2, 3)
# We will make a dictionary using the comprehension and zip:
my_dict = {key: value for key, value in zip(dict_keys, [nr ** 2 for nr in numbers])}
print('New my_dict', my_dict)

print('\n \n \n', 'WEB SCRAPPING')

# WEB SCRAPPING

import requests
from bs4 import BeautifulSoup
import csv

columns = ['position', 'name', 'games', 'goals', 'points']
standings = []

page = requests.get('https://lpf.ro/liga-1')
soup = BeautifulSoup(page.content, features='html.parser')

table = soup.find(id='clasament_ajax_playoff').find('table')
table_rows = table.find_all('tr', class_='echipa_row')
for table_row in table_rows:
    text_from_tds = [
        td.text for td in table_row.find_all('td')
        if 'hiddenMobile' not in td.get('class', []) and td.text
    ]
    team_dict = {col: data for col, data in zip(columns, text_from_tds)}
    standings.append(team_dict)

print(standings)

# Write the received data into a JSON file

with open('standings.json', mode='w') as json_file:
    json.dump(standings, json_file, indent=2)

# Write the received data into a CSV file

with open('standings.csv', mode="w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)
    csv_writer.writerows([team_data.values() for team_data in standings])

# Reading from file

new_standings = []

# Read JSON

with open('standings.json') as json_file:
    new_standings = json.load(json_file)

print('[JSON] standings', new_standings)

# Read CSV

with open('standings.csv') as csv_file:
    new_standings = []
    csv_rows = csv.reader(csv_file)
    csv_rows = list(csv_rows)
    columns = csv_rows[0]

    for row in csv_rows[1:]:
        new_standings = 1
