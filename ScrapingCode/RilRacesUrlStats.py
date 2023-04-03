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
import random


def getsoup(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    return soup

def get_race_info(soup):
    try:
        # infolist
        soup = soup
        # print(soup)
        race_info_tag = soup.find('ul', class_='infolist')
        #print("extraemos info de la carrera")
        table_list_info = race_info_tag.find_all('li')
        for element in range(0, len(table_list_info)):
            try:
                if (element == 0):
                    ######- IMP
                    # date
                    scrp_date = table_list_info[element].find_all('div')
                    #date_converted_string = scrp_date[1].text

                    try:

                        date.append(scrp_date[1].text)
                    except:
                        print("ENTRA EN ERRROR ")
                        print("ENTRA EN ERRROR ")
                        print("ENTRA EN ERRROR ")
                        print("ENTRA EN ERRROR ")
                        date.append("NAN")

                if (element == 1):
                    # hora
                    obtenemos = table_list_info[element].find_all('div')
                if (element == 2):
                    # avg_speed_winner
                    obtenemos = table_list_info[element].find_all('div')
                    velwithkm = obtenemos[1].text
                    velnum = velwithkm.split(" ")
                if (element == 3):
                    # category
                    obtenemos = table_list_info[element].find_all('div')
                    #print(element)
                if (element == 4):
                    # distance
                    scrp_distance = table_list_info[element].find_all('div')
                    try:
                        distance.append(scrp_distance[1].text)
                    except:
                        distance.append(0)

                if (element == 5):
                    # points_scale
                    scrp_points_scale = table_list_info[element].find_all('div')
                    try:
                        points_scale.append(scrp_points_scale[1].text)
                    except:
                        points_scale.append(0)
                if (element == 6):
                    # uci_scale
                    scrp_uci_scale = table_list_info[element].find_all('div')
                    try:
                        uci_scale.append(scrp_uci_scale[1].text)
                    except:
                        uci_scale.append("NAN")
                if (element == 7):
                    # Parcours_type
                    #print(table_list_info[element])
                    obtenemos = table_list_info[element].find_all('div')
                    #print(element)
                    #print(obtenemos[1].split("").getclass)
                    # try:

                    # except:

                if (element == 8):
                    # profile_score
                    scrp_profilescore = table_list_info[element].find_all('div')

                    # try:

                    # except:

                if (element == 9):
                    # vert_meters
                    scrp_vertical_meters = table_list_info[element].find_all('div')

                    try:
                        vert_meters.append(scrp_vertical_meters[1].text)
                    except:
                        vert_meters.append(0)

                if (element == 10):
                    # race_start
                    obtenemos = table_list_info[element].find_all('div')

                if (element == 11):
                    # race_end
                    obtenemos = table_list_info[element].find_all('div')
                if (element == 12):
                    # race_ranking
                    scrp_race_ranking = table_list_info[element].find_all('div')
                    try:
                        race_ranking.append(scrp_race_ranking[1].text)
                    except:
                        race_ranking.append(0)
                if (element == 13):
                    # start_list_quality_score
                    scrp_start_list_quality_score_no_clean = table_list_info[element].find_all('div')
                    scrp_start_list_quality_score = scrp_start_list_quality_score_no_clean[1].find('a')
                    try:
                        start_list_quality_score.append(scrp_start_list_quality_score.text)
                    except:
                        start_list_quality_score.append(0)

                if (element == 14):
                    # won_how
                    scrp_won_how = table_list_info[element].find_all('div')

                    try:
                        won_how.append(scrp_won_how[1].text)
                    except:
                        won_how.append("NAN")

            except:

                  pass

        #print("inforlist")
        # get name of the race
        url_split = race.split('/')
        #print(url_split)
    except:
        print('problemas with ' + race)
    return ('race info extracted')

def get_race_URL(race_name, year, years_back):
    for year in range(int(year), int(year - (years_back + 1)), -1):
        url = 'https://www.procyclingstats.com/race/' + str(race_name) + '/' + str(year) + '/result/result'
        race_URLs.append(url)

    return race_URLs
#races = ['great-ocean-race','strade-bianche','milano-sanremo','omloop-het-nieuwsblad','oxyclean-classic-brugge-de-panne','e3-harelbeke','gent-wevelgem','dwars-door-vlaanderen','ronde-van-vlaanderen','amstel-gold-race','paris-roubaix','la-fleche-wallone','liege-bastogne-liege','Eschborn-Frankfurt','san-sebastian','cyclassics-hamburg','bretagne-classic','gp-quebec','gp-montreal','il-lombardia']

races = ['strade-bianche','milano-sanremo','omloop-het-nieuwsblad','oxyclean-classic-brugge-de-panne','e3-harelbeke','gent-wevelgem','dwars-door-vlaanderen','ronde-van-vlaanderen','amstel-gold-race','paris-roubaix','la-fleche-wallone','liege-bastogne-liege','Eschborn-Frankfurt','san-sebastian','cyclassics-hamburg','bretagne-classic','gp-quebec','gp-montreal','il-lombardia']

#Race_Names_Pave = [ 'paris-roubaix','strade-bianche', 'milano-sanremo', 'ronde-van-vlaanderen', 'paris-roubaix', 'omloop-het-nieuwsblad', 'e3-harelbeke']


race_URLs = []

for race in races:
    get_race_URL(race, 2023, 7)


race_name = []
race_name2 = []
year2 = []

type = []
year = []
age = []
rank = []
team = []
uci = []
name = []
#time = []
date = []
vert_meters = []
quality_score = []
race_ranking = []
start_list_quality_score = []
uci_scale = []
distance = []
points_scale = []
won_how = []



for race in race_URLs[:]:
    try:
        ran =random.randint(4,15)
        time.sleep(ran)
        print(race)
        soup = getsoup(race)
        #print(soup)
        race_table_tag = soup.find('table', class_='results basic moblist10')
        table_element = race_table_tag.find_all('tr')
        #get name of the race
        url_split = race.split('/')
        get_race_info(soup)
        try:
            # RACE_NAME
            race_name2.append(url_split[4])
        except:
            race_name2.append("ERROR")
        try:
            # YEAR
            year2.append(url_split[5])
        except:
            year2.append('0000')
    except:
        print('problemas with '+ race)

    try:
        for i in table_element[1:]:
            try:
                #RACE_NAME
                race_name.append(url_split[4])
            except:
                race_name.append("ERROR")
            try:
                #YEAR
                year.append(url_split[5])
            except:
                year.append('0000')
            try:
                #AGE OF CYCLIST
                age.append(i.find_all('td')[4].text)
            except:
                age.append(0)
            '''
            print(i.find_all('td')[1])
            print(i.find_all('td')[2])
            print(i.find_all('td')[3])
            print(i.find_all('td')[4])
            print(i.find_all('td')[5])
            print(i.find_all('td')[6])
            '''
            try:
                rank.append(i.find_all('td')[0].text)
            except:
                rank.append('0')
            #team_link = str(i.find_all('a')[1]).split('"')[1].split('/')[1]
            #print(team_link)
            # control len -> NULL TEAMS

            #looking for null -
            #TEAM
            try:
                if (len(i.find_all('a')) < 2):
                    team.append("NULL")
                else:
                    team.append(str(i.find_all('a')[1]).split('"')[1].split('/')[1])
                #team.append(i.find_all('td')[4].text)
            except:
                team.append("NAN")
            #UCI POINTS
            try:
                if(i.find_all('td')[6].text== ""):
                    uci.append("0")
                else:
                    uci.append(i.find_all('td')[6].text)
            except:
                uci.append(0)

            #PRIMARY KEY OF THE RIDER
            try:
                name_with_rider = str(i.find('a')).split('"')[1]
                name.append(name_with_rider.split('/')[1])

            except:
                name.append("NAN")

            '''
            # CONTROL THE NULL AND NUMBER ONE
            if (i.find_all('td')[9].find('span') != None):
                time.append(i.find_all('td')[9].find('span').text)
            elif (i.find_all('td', class_="time ar") != None):
                time.append(i.find_all('td', class_="time ar")[0].text)
            else:
                time.append("NULL")
            #time.append(i.find_all('div', class_="hide"))
            '''

    except:
        print('problemas with ' + race)





all_the_info_sec_test = [race_name,name,year,age,rank,team,uci]
info_carrera = [date,distance,vert_meters,race_ranking,start_list_quality_score,uci_scale,points_scale,won_how]


print("vamos a imprimir RESULTADOS:")

for i in all_the_info_sec_test:
    print(len(i))

#print("vamos a imprimir INFO CARRERA:")

for e in info_carrera:
    print(len(e))

Inforace = pd.DataFrame({'Race_Name': race_name2, 'DATE': date ,'Dist': distance,'Vert_meters': vert_meters,'Race_ranking':race_ranking,'Start_list_quality_score':start_list_quality_score,'Uci_scale':uci_scale,'Points_scale':points_scale,'Won_how':won_how,})
LeaderBoard = pd.DataFrame({'Race_Name': race_name, 'Name': name, 'Season': year, 'Age': age, 'Rank': rank, 'Team_Name': team,'UCI':uci, })
LeaderBoard.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\leaderboard.csv', index=False, header=True)
Inforace.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\resultadoscon2023.csv', index=False, header=True)