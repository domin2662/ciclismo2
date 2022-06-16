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


def get_race_URL(race_name, year, years_back):
    for year in range(int(year), int(year - (years_back + 1)), -1):
        url = 'https://www.procyclingstats.com/race/' + str(race_name) + '/' + str(year) + '/result/result'
        race_URLs.append(url)

    return race_URLs


Race_Names_Pave = [ 'paris-roubaix','strade-bianche', 'milano-sanremo', 'ronde-van-vlaanderen', 'paris-roubaix', 'omloop-het-nieuwsblad', 'e3-harelbeke']


race_URLs = []

for race in Race_Names_Pave:
    get_race_URL(race, 2022, 10)



race_name = []
year = []
age = []
rank = []
team = []
uci = []
name = []
time = []



for race in race_URLs[:]:

    soup = getsoup(race)
    race_table_tag = soup.find('table', class_='results basic moblist10')
    table_element = race_table_tag.find_all('tr')
    #get name of the race
    url_split = race.split('/')

    for i in table_element[1:]:
        race_name.append(url_split[4])
        year.append(soup.find('span', class_='hideIfMobile').text)
        age.append(i.find_all('td')[4].text)
        rank.append(i.find_all('td')[0].text)

        #team_link = str(i.find_all('a')[1]).split('"')[1].split('/')[1]
        #print(team_link)
        # control len -> NULL TEAMS

        #looking for null -
        if (len(i.find_all('a')) < 2):
            team.append("NULL")
        else:
            team.append( str(i.find_all('a')[1]).split('"')[1].split('/')[1])
        #team.append(i.find_all('td')[4].text)
        if(i.find_all('td')[6].text== ""):
            uci.append("0")
        else:
            uci.append(i.find_all('td')[6].text)
        #PRIMARY KEY OF THE RIDER
        name_with_rider = str(i.find('a')).split('"')[1]
        name.append(name_with_rider.split('/')[1])
        # CONTROL THE NULL AND NUMBER ONE
        if(i.find_all('td')[9].find('span')!=None):
            time.append(i.find_all('td')[9].find('span').text)
        elif(i.find_all('td', class_="time ar")!=None):
            time.append(i.find_all('td', class_="time ar")[0].text)
        else:
            time.append("NULL")

        #time.append(i.find_all('div', class_="hide"))



LeaderBoard = pd.DataFrame({'Race_Name': race_name, 'Name': name, 'Season': year, 'Age': age,
                            'Rank': rank, 'Team_Name': team,'UCI':uci,'Finishing_Time': time})

LeaderBoard.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\LeaderBoard_Data.csv', index=False, header=True)