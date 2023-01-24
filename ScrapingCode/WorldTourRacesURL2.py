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
import time
from random import seed
from random import randint

def getsoup(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    return soup

years = ['2022','2021','2020','2019','2018','2017','2016','2015','2014','2013','2012']
UCI_Circuit=['1','2','13','11','14','18']
url_races=[]
races_id = []
winners_id = []
category =[]
year = []
for ye in years:
    for ci in UCI_Circuit:
        value = randint(0, 10)
        time.sleep(value)
        url_updated = 'https://www.procyclingstats.com/races.php?year=' + ye +'&circuit='+ ci +'1&class=&filter=Filter'
        soup = getsoup( url_updated)
        print(soup.find('td',class_="hide cs500"))

        race_table_tag = soup.find('table', class_='basic')
        table_element = race_table_tag.find_all('tr')


        for i in table_element[1:]:
            year.append(ye)
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

races = pd.DataFrame({'year':year ,'race_id': races_id,'winner_id':winners_id,'category':category })

print(urlraces)
print(races)



urlraces.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\Url_races2.csv', index=False, header=True)

races.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\Url_Races_winner_10_Years_Categorys.csv', index=False, header=True)