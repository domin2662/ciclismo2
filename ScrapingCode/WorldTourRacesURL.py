from turtle import st

import requests
import lxml
import csv
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime as dt
import pprint
import sqlite3
pd.__version__


def getsoup(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    return soup


soup = getsoup("https://www.procyclingstats.com/calendar/year-calendar")
print(soup.find('td',class_="hide cs500"))

race_table_tag = soup.find('table', class_='basic')
table_element = race_table_tag.find_all('tr')
url_races=[]
races_id = []
winners_id = []
category =[]
year = []

for i in table_element[1:]:
    #EXTRACT URLS OF RACES & RACESID
    if (len(i.find_all('td')[2].find('a')) < 1):
        pass
    else:
        rac =str(i.find_all('td')[2].find('a'))
        race =  rac.split('"')[1]
        url ="https://www.procyclingstats.com/"+ race
        url_races.append(url)
        raceextractorid = race.split("/")[1]
        races_id.append(raceextractorid)
    #EXTRACT ID OF RIDERS
    if(len(i.find_all('td')[3].find('a')) < 1):
        winners_id.append("NULL")
        print("NULL")
    else:
        print(i.find_all('td')[3].find('a'))
        a_rider_url = str(i.find_all('td')[3].find('a'))
        rider_url = a_rider_url.split('"')[1]
        rider_id = rider_url.split("/")[1]
        winners_id.append(rider_id)
        print(rider_id)
    category.append(i.find_all('td')[4].text)

urlraces = pd.DataFrame({'races_url': url_races, })

races = pd.DataFrame({'race_id': races_id,'winner_id':winners_id,'category':category })

print(urlraces)
print(races)



urlraces.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\Url_races.csv', index=False, header=True)

races.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\Race_by_year.csv', index=False, header=True)