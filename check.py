# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:13:57 2019

@author: intel
"""

import requests
import html5lib
from bs4 import BeautifulSoup as BS
import pandas as pd

response = requests.get('https://en.wikipedia.org/wiki/List_of_Regional_Transport_Office_districts_in_India')
#print(response.content)
soup = BS(response.content,'html5lib')
#print(soup)
divoftables = soup.find('div',attrs = {'class':'mw-parser-output'})
#print(divoftables)

listofstates = []
for table in divoftables.findAll('table',attrs = {'class':'wikitable'}):
    listofdist = []
    for td in table.findAll('td'):
        listofdist.append(td.text)
    
    newli = [x for x in listofdist if x != '\n']
    listofstates.append(newli)
print(listofstates)
#print(len(listofstates))
a = 0
b = 3
alist = []
for i in range(len(listofstates[0])):
    #alist = []
    if a < len(listofstates[0]) and b < len(listofstates[0]):
        alist.append(listofstates[0][a])
        alist.append(listofstates[0][b])
        a += 4
        b += 4
print(alist)
import re
pattern = 'KL-(\d){2}'#18
pattern = 'MH-(\d){2}'#20
#pattern = 'GJ-(\d){1,2}' 
#pattern = 'CH-(\d){2}'
#pattern = 'CG-(\d){2}'
#pattern = 'AR-(\d){2}'
#pattern = 'AR-(\d){2}'
#pattern = 'BR-(\d){2}'
codelist = []
for stringc in listofstates[18]:
    if re.search(pattern, stringc):
        codelist.append(stringc.rstrip('\n'))
    else:
        pass
print(codelist)   
districtlist = []
import string
for stringc in listofstates[18]:
    if stringc != 'RLA\n' and string != 'ARTO\n' and stringc != 'RTO\n' and not(re.search(pattern,stringc)):
        districtlist.append(stringc.rstrip('\n'))
    else:
        pass
print(districtlist.pop())
print(listofstates[3])#manual part
#DL manually (6,7,8)
#Goa GA manually(10)
#HP (11) no district after name

print(districtlist)
#print(listofstates[18])
print(len(codelist),len(districtlist))
codelist.append(districtlist.pop(len(districtlist)-2))
print(codelist,districtlist)
print(len(codelist),len(districtlist))
dictionaryLD = dict(zip(codelist,districtlist))
print(dictionaryHR)
import json
with open('vehiclecodefile.json','a') as file:
   json.dump(dictionaryLD,file)
#'HP-03\n', 'RLA\n', 'Shimla – Urban\n', 'HP-04\n', 'RLA\n', 'Dharamsala\n', 'HP-05\n', 'RLA\n', 'Mandi\n', 'HP-06\n', 'RLA\n', 'Rampur Bushahr\n', 'HP-07\n', 'RLA\n', 'Shimla\n', 'HP-08\n', 'RLA\n', 'Chaupal\n', 'HP-09\n', 'RLA\n', 'Theog\n', 'HP-10\n', 'RLA\n', 'Rohru\n', 'HP-11\n', 'RLA\n', 'Arki\n', 'HP-12\n', 'RLA\n', 'Nalagarh\n', 'HP-13\n', 'RLA\n', 'Kandaghat\n', 'HP-14\n', 'RLA\n', 'Solan\n', 'HP-15\n', 'RLA\n', 'Parwanoo\n', 'HP-16\n', 'RLA\n', 'Rajgarh\n', 'HP-17\n', 'RLA\n', 'Paonta Sahib\n', 'HP-18\n', 'RLA\n', 'Nahan\n', 'HP-19\n', 'RLA\n', 'Amb\n', 'HP-20\n', 'RLA\n', 'Una (1)\n', 'HP-21\n', 'RLA\n', 'Barsar, Hamirpur\n', 'HP-22\n', 'RLA\n', 'Hamirpur\n', 'HP-23\n', 'RLA\n', 'Ghumarwin\n', 'HP-24\n', 'RLA\n', 'Bilaspur\n', 'HP-25\n', 'RLA\n', 'Reckong Peo\n', 'HP-26\n', 'RLA\n', 'Nichar (Bhaba Nagar)\n', 'HP-27\n', 'RLA\n', 'Poo\n', 'HP-28\n', 'RLA\n', 'Sarkaghat\n', 'HP-29\n', 'RLA\n', 'Jogindernagar\n', 'HP-30\n', 'RLA\n', 'Karsog\n', 'HP-31\n', 'RLA\n', 'Sundernagar\n', 'HP-32\n', 'RLA\n', 'Gohar, Mandi\n', 'HP-33\n', 'RLA\n', 'Mandi\n', 'HP-34\n', 'RLA\n', 'Kullu\n', 'HP-35\n', 'RLA\n', 'Anni, Kullu\n', 'HP-36\n', 'RLA\n', 'Dehra\n', 'HP-37\n', 'RLA\n', 'Palampur\n', 'HP-38\n', 'RLA\n', 'Nurpur\n', 'HP-39\n', 'RTO\n', 'Dharamshala\n', 'HP-40\n', 'RTO\n', 'Kangra\n', 'HP-41\n', 'RLA\n', 'Kaza\n', 'HP-42\n', 'RLA\n', 'Keylong\n', 'HP-43\n', 'RLA\n', 'Udaipur\n', 'HP-44\n', 'RLA\n', 'Churah\n', 'HP-45\n', 'RLA\n', 'Pangi\n', 'HP-46\n', 'RLA\n', 'Bharmour\n', 'HP-47\n', 'RLA\n', 'Dalhousie\n', 'HP-48\n', 'RLA\n', 'Chamba (1)\n', 'HP-49\n', 'RLA\n', 'Banjar\n', 'HP-50\n', 'Shimla (auto-rikshaws)\n', 'HP-51 & HP-52\n', 'RTO\n', 'Shimla (urban)\n', 'HP-53\n', 'RLA\n', 'Baijnath\n', 'HP-54\n', 'RLA\n', 'Jawali\n', 'HP-55\n', 'RLA\n', 'Nadaun / Hamirpur\n', 'HP-56\n', 'RLA\n', 'Jaisinghpur\n', 'HP-57\n', 'RLA\n', 'Chowari\n', 'HP-58\n', 'RLA\n', 'Manali\n', 'HP-59\n', 'RLA\n', 'Solan\n', 'HP-60\n', 'RLA\n', 'Hamirpur\n', 'HP-61\n', 'RLA\n', 'Kullu\n', 'HP-62 & HP-63\n', 'RTO\n', 'Shimla (rural)\n', 'HP-64\n', 'RTO\n', 'Solan\n', 'HP-65\n', 'RLA\n', 'Mandi\n', 'HP-66\n', 'RTO\n', 'Kullu\n', 'HP-67\n', 'RTO\n', 'Hamirpur\n', 'HP-68\n', 'RTO\n', 'Dharmsala\n', 'HP-69 & HP-70\n', 'RTO\n', 'Bilaspur\n', 'HP-71\n', 'RTO\n', 'Nahan\n', 'HP-72\n', 'RTO\n', 'Una (2)\n', 'HP-73\n', 'RTO\n', 'Chamba (2)\n', 'HP-74\n', 'RLA\n', 'Bhoranj, Hamirpur\n', 'HP-76\n', 'RLA\n', 'Paddhar, Mandi\n', 'HP-77\n', 'RLA\n', 'Dodra Kawar, Shimla\n', 'HP-78\n', 'RLA\n', 'Bangana, Una\n', 'HP-79\n', 'RLA\n', 'Sangrah, Sirmaur\n', 'HP-80\n', 'RLA\n', 'Haroli, Una\n', 'HP-81\n', 'RLA\n', 'Salooni (Dist. Chamba)\n', 'HP-82\n', 'RTO\n', 'Mandi (rural)\n', 'HP-83\n', 'RLA\n', 'Jawalaji, Kangra\n', 'HP-84\n', 'RLA\n', 'Sujanpur Tihra, Hamirpur\n', 'HP-85\n', 'RLA\n', 'Shillai, Sirmaur\n', 'HP-86\n', 'RLA\n', 'Dharampur, Mandi\n', 'HP-87\n', 'RLA\n', 'Janjehli, Mandi\n', 'HP-88\n', 'RLA\n', 'Fatehpur, Kangra\n', 'HP-89\n', 'RLA\n', 'Jhandutta, Bilaspur\n', 'HP-90\n' 'RLA\n', 'Shahpur\n', 'HP-91\n', 'RLA\n', 'Naina Devi (Swarghat)\n', 'HP-92\n', 'RTO\n', 'Rampur Bushahr\n', 'HP-93\n', 'RLA\n', 'Baddi\n', 'HP-95\n', 'RLA\n', 'Kumarsain\n'],
    
        
#['AP-02\n', 'RTO\n', 'Anantapur\n', 'Anantapur District\n', 'AP-03\n', 'DTC\n', 'Chittoor\n', 'Chittoor district\n', 'AP-04\n', 'DTC\n', 'Kadapa\n', 'YSR Kadapa district\n', 'AP-05&06\n', 'DTC\n', 'Kakinada\n', 'East Godavari district\n', 'AP-07, 08\n', 'DTC\n', 'Guntur\n', 'Guntur district\n', 'AP-16\n', 'DTC\n', 'Vijayawada\n', 'Krishna district\n', 'AP-18\n', 'DTC\n', 'Vijayawada\n', 'Krishna district\n', 'Used for Andhra Pradesh Police Vehicles\n', 'AP-21\n', 'DTC\n', 'Kurnool\n', 'Kurnool district\n', 'AP-26\n', 'DTC\n', 'Nellore\n', 'Nellore district\n', 'AP-27\n', 'RTO\n', 'Ongole\n', 'Prakasam district\n', 'AP-30\n', 'DTC\n', 'Srikakulam\n', 'Srikakulam district\n', 'AP-31\n', 'DTC\n', 'Visakhapatnam\n', 'Visakhapatnam district\n', 'AP-32\n', 'DTC\n', 'Visakhapatnam\n', 'Visakhapatnam district\n', 'AP-33\n', 'RTO\n', 'Anakapalle\n', 'Visakhapatnam district\n', 'AP-34\n', 'RTO\n', 'Narsipatnam\n', 'Visakhapatnam district\n', 'AP-35\n', 'RTO\n', 'Vizianagaram\n', 'Vizianagaram district\n', 'AP-37\n', 'DTC\n', 'Eluru\n', 'West Godavari district\n', 'AP-39\n', 'DTCs, RTOs\n', 'All districts (from 30 January 2019 onwards)[1]
    
    
    
    

    



