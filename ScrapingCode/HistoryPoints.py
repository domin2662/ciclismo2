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

URLs = pd.read_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\RiderProfile_URLs2.csv', index_col=0)
print(URLs)

###############################################################

#st.title("DOMIN CYCLING ")
#st.dataframe(URLs)


name = []
height = []
weight = []
nationality = []
id_rider =[]
name = []
height = []
weight = []
nationality = []

for rider in URLs.iterrows():
    a = rider[0]
    soup = getsoup(a)
    main = ([i.text for i in soup.find('div', class_='main')])
    id_rider_to_clean = a.split('/');
    id_rider_to_add = id_rider_to_clean[-1]
    id_rider.append(id_rider_to_add)
    name.append(main[2])
    rdr_info_tag = soup.find('div', class_='rdr-info-cont')
    info_list = [i for i in rdr_info_tag]
    rit_element = rdr_info_tag.find_all('span')

    span_list = [i for i in rit_element[1]]

    try:
        weight.append(span_list[1])
    except IndexError:
        weight.append('NaN')

    try:
        span_tag = [i for i in span_list[2]]
        height.append(span_tag[1])
    except IndexError:
        height.append('NaN')

    try:
        nationality.append(info_list[8].text)

    except IndexError:
        nationality.append('NaN')


climber = []
gc = []
tt = []
sprint = []
one_day_races = []

for rider in URLs.iterrows():
    print(rider)
    a = rider[0]
    soup = getsoup(a)
    ## select
    bs4elementTag = [i for i in soup.find('ul', class_='basic')]

    try:
        one_day_races.append(bs4elementTag[0].text.replace('One day races', ''))
    except:
        one_day_races.append('0')
    try:
        gc.append(bs4elementTag[2].text.replace('GC', ''))
    except:
        gc.append('0')
    try:
        tt.append(bs4elementTag[4].text.replace('Time trial', ''))
    except:
        tt.append('0')
    try:
        sprint.append(bs4elementTag[6].text.replace('Sprint', '') )
    except:
        sprint.append('0')
    try:
        climber.append(bs4elementTag[8].text.replace('Climber', ''))
    except:
        climber.append('0')


#callum-scotson,Callum  Scotson, 1.84 m, 77 kg   ,Australia,25Climber,93GC,40Time trial,49Sprint,17One day races


Profile = pd.DataFrame({'Rider_id': id_rider,  'Name': name, 'Height': height, 'Weight': weight, 'Nationality': nationality,
                        'Climbing': climber, 'General_Classification': gc, 'Time_Trial': tt, 'Sprint': sprint,
                        'One_Day_Races': one_day_races})

Profile.to_csv(r'C:\Users\DOMIN2662\PycharmProjects\ciclismo2\BBDDcsv\Profile_Data2.csv', index=False, header=True)