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
import streamlit as st
import re


def getsoup(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')

    return soup



URLs = pd.read_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\RiderProfile_URLs2.csv')
URLs = list(URLs['0'])
season_urls = [i + str('/statistics/season-statistics') for i in URLs]
len(season_urls)




Season = []
Points = []
Racedays = []
KMs_Rode = []
Wins = []
Top_10s = []
Rider_Name = []

for rider in season_urls:
    #print(rider)
    soup = getsoup(rider)
    rdr_table_tag = soup.find('table', class_='basic')
    table = rdr_table_tag.find_all('tr')

    #print(table)
    stat_list = []
    for season in table[1:-1]:
        statseason =[]
        for stat in season:
            if(stat.text =="-"):
                statseason.append(0)
                #print(stat.text)
            else:
                statseason.append(float(stat.text))
                #print(stat.text)
        stat_list.append(statseason)

    #print(stat_list)


    #stat_list = [int(stat.text) for season in table[1:-1] for stat in season]

    #stat_by_season = [stat_list[i:i + 6] for i in range(0, len(stat_list), 6)]

    for year in stat_list:
        #print(year)
        Season.append(year[0])
        Points.append(year[1])
        Racedays.append(year[2])
        KMs_Rode.append(year[3])
        Wins.append(year[4])
        Top_10s.append(year[5])
        name = rider.replace('https://www.procyclingstats.com/rider/', '').replace('/statistics/season-statistics', '')
        Rider_Name.append(name)
        #Rider_Name.append(name.replace('-', ' '))

SeasonStats = pd.DataFrame({'Rider_Name': Rider_Name, 'Season': Season,
                            'Points': Points, 'Racedays': Racedays, 'KMs_Rode': KMs_Rode, 'Wins': Wins,
                            'Top_10s': Top_10s})

SeasonStats.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\SeasonStats2.csv', index=False,  header=True)