import psycopg2
import pandas as pd
import re
import CyclistController
import RacesController

#CHARGE THE DATA FROM THE CSV & INSERT ALL
def insert_clean_the_data_cyclist():
    profiles = pd.read_csv('../BBDDcsv/Profile_Data12.csv', header=0)
    profiles = profiles.reset_index()  # make sure indexes pair with number of rows
    print(profiles.head())
    for index, row in profiles.iterrows():
        #Rider_id,Name,Height,Weight,Nationality,Climbing,General_Classification,Time_Trial,Sprint,One_Day_Races
        #mauro-finetto,Mauro  Finetto, 1.77 m, 62 kg   ,Italy,1002Climber,1199GC,229Time trial,1787Sprint,2156One day races

        id_cyclist = row['Rider_id']
        rider_name = row['Name']
        try:
            height_to_convert = row['Height'].split(" ")
            height =float( height_to_convert[1])
        except:
            height =0
        try:
            weight_to_convert = row['Weight'].split(" ")
            weight =weight_to_convert[1]
        except:
            height =0

        try:
            nationality = row['Nationality']
        except:
            nationality = 'NULL'

        try:
            nationality = row['Nationality']
        except:
            nationality = 'NULL'
        #EXTRACT ONLY DIGITS
        general_classification =re.findall(r'\d+', row['General_Classification'])
        print(general_classification[0])
        general_classification = int(general_classification[0])
        time_trial = re.findall(r'\d+', row['Time_Trial'])
        time_trial = int(time_trial[0])
        sprint = re.findall(r'\d+', row['Sprint'])
        sprint = int(sprint[0])
        climbing =  re.findall(r'\d+', row['Climbing'])
        climbing = int(climbing[0])
        one_day_races = re.findall(r'\d+', row['One_Day_Races'])
        one_day_races = int(one_day_races[0])
        print([id_cyclist, rider_name, weight, nationality, general_classification, time_trial, climbing, sprint,one_day_races, height])
        #ADD CYCLIST INTO DATABASE
        CyclistController.addonecyclist(id_cyclist, rider_name, weight, nationality, general_classification, time_trial, climbing, sprint,one_day_races, height)

def riders_per_season():

    #Rider_Name, Season, Points, Racedays, KMs_Rode, Wins, Top_10s
    #mauro-finetto, 2021.0, 59.0, 30.0, 4793.0, 0.0, 0.0
    riders_season = pd.read_csv('../BBDDcsv/SeasonStats2.csv', header=0)
    riders_season =  riders_season.reset_index()  # make sure indexes pair with number of rows
    print(riders_season.head())
    for index, row in riders_season.iterrows():

        id_cyclist = row["Rider_Name"]
        season = int(row["Season"])
        point = int(row["Points"])
        race_days = int(row["Racedays"])
        kms_rode = int(row["KMs_Rode"])
        wins = int(row["Wins"])
        tops_10 = int(row["Top_10s"])
        print([id_cyclist, season, point, race_days, kms_rode, wins, tops_10])
        CyclistController.add_rider_historic_results(id_cyclist, season, point, race_days, kms_rode, wins, tops_10)



def races_per_season():
    races = pd.read_csv('../BBDDcsv/Race_by_year.csv', header=0)
    races = races.reset_index()  # make sure indexes pair with number of rows
    print(races.head())
    for index, row in races.iterrows():
        #race_id, winner_id, category
        #tour - down - under, NULL, 2.UWT
        print(row["race_id"])
        print(row["category"])

        RacesController.addrace(row["race_id"],row["category"],"")

def races_results():
    races_clasification = pd.read_csv('../BBDDcsv/LeaderBoard_Data.csv')
    races_clasification = races_clasification.reset_index()  # make sure indexes pair with number of rows
    print(races_clasification.head())
    for index, row in races_clasification.iterrows():
        #Race_Name, Name, Season, Age, Rank, Team_Name, UCI, Finishing_Time
        #paris - roubaix, dylan - van - baarle, 2022, 29, 1, ineos - grenadiers - 2022, 500, 5: 37:00
        # id_race, id_cyclist, season, age, team_name, uci, finishing_time, rank
        if(row["Rank"]== 'DNF'):
            result = 0
        elif (row["Rank"]== 'OTL'):
            result = 0
        else:
            result =row["Rank"]
        RacesController.add_one_race_result(row["Race_Name"],row["Name"],row["Season"],row["Age"],row["Team_Name"],row["UCI"],row["Finishing_Time"],result)

races_results()
#riders_per_season()
#races_per_season()


