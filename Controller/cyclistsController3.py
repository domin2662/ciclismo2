# Example python program to read data from a PostgreSQL table

# and load into a pandas DataFrame

import psycopg2
import streamlit as st

import pandas as pds

from sqlalchemy import create_engine

# Create an engine instance

def get_dataframe_all_cyclists():

    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_cyclists = pds.read_sql("select * from cyclists" , dbConnection);
    pds.set_option('display.expand_frame_repr', False);

    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_cyclists

def get_dataframe_cyclist(rider_id):
    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_selected = pds.read_sql("select id_cyclist, rider_name, weight, nationality, general_classification, time_trial, climbing, sprint, one_day_races, height from cyclists where id_cyclist='"+rider_id +"'" , dbConnection);
    pds.set_option('display.expand_frame_repr', False);
    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_selected

def get_dataframe_all_cyclists_by_seson():

    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_cyclists = pds.read_sql("select * from rider_historic_results" , dbConnection);
    pds.set_option('display.expand_frame_repr', False);

    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_cyclists

def get_dataframe_nationality():
    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_nationality = pds.read_sql("select DISTINCT nationality from cyclists",dbConnection);
    pds.set_option('display.expand_frame_repr', False);
    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_nationality