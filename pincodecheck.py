# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:48:16 2019

@author: intel
"""
import requests
import html5lib
from bs4 import BeautifulSoup as BS
import pandas as pd

response = requests.get('http://www.postalpincode.in/Search-By-Location?StateId=28')
#print(response.content)
soup = BS(response.content,'html5lib')
#print(soup)
al =[]
for i in soup.findAll('table', attrs = {'class':'DDGridView'}):
    for a in i.findAll('td'):
        al.append(a.text.strip())
print(al)
