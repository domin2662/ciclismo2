import pandas as pds

from sqlalchemy import create_engine

import psycopg2
import streamlit as st

import pandas as pds



# Create an engine instance

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()



# Create an engine instance

def get_dataframe_all_race_results():

    dataFrame_race_results =pds.read_sql("select  id_race, id_cyclist, season, age, team_name, uci, rank from race_results", conn)
    pds.set_option('display.expand_frame_repr', False);
    return dataFrame_race_results

def get_dataframe_race_results_classics_team_season(team):

    dataFrame_race_results_classics = pds.read_sql( "select  id_race, id_cyclist, season, age, team_name, uci, rank from race_results where team_name='" + team + "'", conn)
    pds.set_option('display.expand_frame_repr', False);
    return dataFrame_race_results_classics

def get_dataframe_season():

    dataFrame_season = pds.read_sql("select DISTINCT season from race_results ORDER BY season ", conn)
    pds.set_option('display.expand_frame_repr', False);
    return dataFrame_season

def get_dataframe_teams(season):

    dataFrame_teams =pds.read_sql("select DISTINCT team_name from race_results where season='"+ season +"'",conn)
    pds.set_option('display.expand_frame_repr', False);
    return  dataFrame_teams
