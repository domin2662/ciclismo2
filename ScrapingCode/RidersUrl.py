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
    #print(soup)
    return soup


def get_rider_urls(race_name, year, years_back):
    urls = []

    for year in range(int(year), int(year - (years_back + 1)), -1):

        race_url = 'https://www.procyclingstats.com/race/' + str(race_name) + '/' + str(year) + '/result'
        soup = getsoup(race_url)

        race_table_tag = soup.find('table', class_='results basic moblist10')
        tr_table = race_table_tag.find_all('tr')

        rider_name = []

        for i in tr_table[1:]:
            a_tag = i.find_all('a')[0]
            rider_name.append(a_tag['href'])

        urls.append(['https://www.procyclingstats.com/' + j for j in rider_name])
        #print(urls)

    return urls


races = ['gent-wevelgem', 'strade-bianche', 'milano-sanremo',
         'ronde-van-vlaanderen', 'paris-roubaix', 'omloop-het-nieuwsblad', 'e3-harelbeke']

races_22 = ['gent-wevelgem', 'strade-bianche', 'milano-sanremo',
            'ronde-van-vlaanderen', 'omloop-het-nieuwsblad', 'e3-harelbeke']

url_list = [get_rider_urls(i, 2022, 13) for i in races]
flat_url = [item for sublist in url_list for subsublist in sublist for item in subsublist]

races_22 = [get_rider_urls(i, 2022, 0) for i in races_22]
flat_22 = [item for sublist in races_22 for subsublist in sublist for item in subsublist]

flat_url = flat_url + flat_22

unique_URLs = list(set(flat_url))
unique_URLs = pd.Series(unique_URLs)

unique_URLs.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\RiderProfile_URLs2.csv', index=False, header=True)

#URLs = pd.read_csv('RiderProfile_URLs.csv')
