# Example python program to read data from a PostgreSQL table

# and load into a pandas DataFrame

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
#Test
#cambio2

def get_dataframe_all_cyclists():
    dataFrame_cyclists = pds.read_sql("select * from cyclists",conn);
    pds.set_option('display.expand_frame_repr', False);

    return dataFrame_cyclists

def get_dataframe_cyclist(rider_id):
    dataFrame_selected = pds.read_sql("select id_cyclist, rider_name, weight, nationality, general_classification, time_trial, climbing, sprint, one_day_races, height from cyclists where id_cyclist='"+rider_id +"'",conn );
    pds.set_option('display.expand_frame_repr', False);

    return dataFrame_selected

def get_dataframe_all_cyclists_by_seson():
    dataFrame_cyclists = pds.read_sql("select * from rider_historic_results",conn );
    pds.set_option('display.expand_frame_repr', False);

    return dataFrame_cyclists

def get_dataframe_nationality():
    dataFrame_nationality = pds.read_sql("select DISTINCT nationality from cyclists",conn);
    pds.set_option('display.expand_frame_repr', False);

    return dataFrame_nationality