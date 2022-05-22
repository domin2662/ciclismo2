import psycopg2
import pandas as pd
import re


def getatrib():
    info=[]
    with open('../confBBDD.ini', 'r') as f:
        for line in f:
            p = line.split("=")
            if(len(p)==2):
                p[1]=p[1].rstrip('\n')
                info.append(p[1])
    print(info)
    return info


def addonecyclist(id_cyclist,rider_name,weight,nationality,general_classification,time_trial,climbing,sprint,one_day_races,height):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar= "INSERT INTO public.cyclists(id_cyclist, rider_name, weight, nationality, general_classification, time_trial, climbing, sprint, one_day_races, height) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values=(id_cyclist,rider_name,weight,nationality,general_classification,time_trial,climbing,sprint,one_day_races,height)
        cur.execute(insertar,values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def updatecyclist(id_cyclist,general_classification,time_trial,climbing,sprint,one_day_races):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar = "UPDATE public.cyclists SET  general_classification= %s, time_trial= %s, climbing= %s, sprint= %s, one_day_races= %s   WHERE id_cyclist = %s"
        values = ( general_classification, time_trial, climbing, sprint,one_day_races, id_cyclist)
        cur.execute(insertar, values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def add_rider_historic_results(id_cyclist, season, point, racedays, kms_rode, wins, toptens):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar = "INSERT INTO public.rider_historic_results(id_cyclist, season, point, racedays, kms_rode, wins, toptens) VALUES( %s, %s, %s, %s, %s, %s, %s)"
        values = (id_cyclist, season, point, racedays, kms_rode, wins, toptens)
        cur.execute(insertar, values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def update_rider_historic_results(hitoric_id,id_cyclist, season, point, racedays, kms_rode, wins, toptens):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar = "UPDATE public.rider_historic_results SET hitoric_id=?, id_cyclist=?, season=?, point=?, racedays=?, kms_rode=?, wins=?, toptens=? WHERE <condition>; %s)"
        values = (id_cyclist, season, point, racedays, kms_rode, wins, toptens,hitoric_id)
        cur.execute(insertar, values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')