# https://www.topcoder.com/thrive/articles/web-scraping-with-beautiful-soup
from bs4 import BeautifulSoup
import requests
import pandas as pd

# beautiful objects are created using "html.parser"
# crawling is urls, scraping is data
url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
result = requests.get(url_link).text
soup = BeautifulSoup(result, 'html.parser')
# print(doc.prettify())

# must reference the table class
# verifying tables and their classes
# print('Classes for each table:')
# for table in soup.find_all('table'):
#     print(table.get('class'))

# note: class name is case and space sensitive
my_table = soup.find('table', class_="wikitable sortable plainrowheaders")

# extract all th tags, table headers
th_tags = my_table.find_all('th')
#print(th_tags)

# create empty string where the scrapped data will be stored
names = []
for elem in th_tags:
    a_tags = elem.find_all("a")
    for i in a_tags:
        names.append(i.string)
    print(names)

# Removing the numbers to remain with the states only
final_list = names[9: ]
# names[9: ]means from index 9 in the list
states = []
for str in final_list:
  if len(str) > 3:
    states.append(str)
print(states)

# Getting population from table
lation = my_table.find_all("div")
pop = []
for i in lation:
    pop.append(i.string)
print(pop)

# removing strings in between
population = []
for i in pop:
    if len(i)> 3:
        population.append(i)
print(population)


# Writing DATA TO CSV
usPop = pd.DataFrame()

usPop['state'] = states
usPop['population'] = population

print(usPop)

usPop.to_csv('us_statewise_population.csv')
