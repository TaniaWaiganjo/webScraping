# Web scraping library allowing parse and scrape html and xml pages using a parser
# requests library for http methods++ using json method, can read more on it
#from cgitb import text

import requests
# assign the website url to a variable
url_link = 'https://wikileaks.org/dealmaker/Al-Yousef/'

# storing html data in python object
result = requests.get(url_link).text
# without the .text it returns code 200 if successful
print(result)



