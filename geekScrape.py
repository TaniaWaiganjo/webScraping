# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
# API to extract data eg. facebook using graph API

# parser libraries eg. html5lib
# parser extracts nested data

import requests
from bs4 import BeautifulSoup
url_link = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(url_link)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# html5lib or html.parser
print(soup.prettify())

# You may need to add a browser agent when error 'not accepted occurs'


quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.find_all('div',attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)