# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:37:59 2019

@author: intel
"""

import requests
import html5lib
from bs4 import BeautifulSoup as BS
import pandas as pd

response = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population')
#print(response.content)
soup = BS(response.content,'html5lib')
#print(soup)
divoftables = soup.find('div',attrs = {'class':'mw-parser-output'})
#print(divoftables)

listo = []
for table in divoftables.findAll('table',attrs = {'class':'wikitable'}):
    for td in table.findAll('td'):
        listo.append(td.text)
print(len(listo))
a,b = 1,2
newl = []
for i in range(1,300):
    newl.append(tuple(listo[a:b+1]))
    a += 5
    b += 5
print(dict(newl))

    











