import pandas as pds

from sqlalchemy import create_engine

# Create an engine instance

def get_dataframe_all_race_results():

    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_race_results = pds.read_sql("select * race_results" , dbConnection);
    pds.set_option('display.expand_frame_repr', False);

    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_race_results

def get_dataframe_race_results_classics_team_season(team):
    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_race_results_classics = pds.read_sql("select id_result, id_race, id_cyclist, season, age, team_name, uci, finishing_time, rank from race_results where team_name='"+ team +"'"  , dbConnection);
    pds.set_option('display.expand_frame_repr', False);
    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_race_results_classics

def get_dataframe_season():
    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_season = pds.read_sql(
        "select DISTINCT season from race_results ORDER BY season ",
        dbConnection);
    pds.set_option('display.expand_frame_repr', False);
    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return dataFrame_season

def get_dataframe_teams(season):
    alchemyEngine = create_engine('postgresql+psycopg2://postgres:openpgpwd@127.0.0.1/cycling', pool_recycle=3600)
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();

    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame_teams = pds.read_sql(
        "select team_name from race_results where season='"+season+"'",
        dbConnection);
    pds.set_option('display.expand_frame_repr', False);
    # Print the DataFrame
    # Close the database connection
    dbConnection.close();
    return  dataFrame_teams
