import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from st_aggrid import AgGrid
import altair as alt
from st_aggrid import AgGrid
import pandas as pd
import Controller.cyclistsController as CyController
import Controller.racesController as rcController
from streamlit_echarts import st_echarts, st_pyecharts
#################LOAD INFORMATION CSV ##########################

competitionsstats = pd.read_csv('BBDDcsv/LeaderBoard_Data.csv', header=0)
estadisticas = pd.read_csv('BBDDcsv/SeasonStats2.csv', header=0)


################ LOAD INFORMATION POSTGRES #############################
profiles = CyController.get_dataframe_all_cyclists()
seasons = rcController.get_dataframe_season()


###############TITULO##################
st.set_page_config(layout="wide")
st.image('bike.jpg')
###########  SIDEBAR MENU   ##########
st.sidebar.title(":bike:CIDEAM CYCLING")
typeofcompetition = st.sidebar.radio("Type of Competition", ('Climber', 'GC', 'Time trial', 'Sprint', 'One day races'))
rider = st.sidebar.selectbox('SELECT A RIDER', profiles)
multirider = st.sidebar.multiselect('SELECT A RIDER', profiles)
number_cyclist_selected = st.sidebar.slider("Number of cyclist",1,200,40)
season = st.sidebar.selectbox('SELECT A SEASON', seasons)



##### OPTION WITH PANDAS #################
#result =profiles.loc[profiles[cols_to_check][0] == rider]
#result = profiles.loc[profiles['Rider_id'].str.contains(str(rider), case=False)]

################# CENTRAL MENU ########################
# FILTER RESULT WIT POSTGRES
result= CyController.get_dataframe_cyclist(str(rider))
st.dataframe(profiles)
AgGrid(profiles)

#######HEADING ##############

col1, col2 = st.columns([3, 2])


with col1:
    st.subheader("ALL THE CYCLIST")

with col1:
    st.subheader("SELECTED : " + str(rider).upper())
    st.dataframe(result)

with col2:
    st.subheader("R history : " + str(rider).upper())

    


    option = {
        "radar": {
            "indicator": [
                {"name": "CLIMBER", "max": 18842},
                {"name": "G C", "max": 13292},
                {"name": "TIME TRIAL", "max": 12010},
                {"name": "SPRINT", "max": 20262},
                {"name": "ONE DAY RACES", "max": 15485},

            ]
        },
        "series": [
            {
                "name": "预算 vs 开销（Budget vs spending）",
                "type": "radar",

                "data": [
                    {
                        "value": [int(result.iat[0,5]), int(result.iat[0,6]), int(result.iat[0,7]), int(result.iat[0,8]), int(result.iat[0,9])],
                        "name": "预算分配（Allocated Budget）",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="300px")


################## WORKING WITH PANDAS #########################

uniqueId = estadisticas["Rider_Name"].unique()
uniqueSeason = estadisticas["Season"].unique()
estadisticas['Season'] = estadisticas['Season'].astype(int)
estadisticas['Points'] = estadisticas['Points'].astype(int)
estadisticas['Racedays'] = estadisticas['Racedays'].astype(int)
estadisticas['KMs_Rode'] = estadisticas['KMs_Rode'].astype(int)
estadisticas['Wins'] = estadisticas['Wins'].astype(int)
estadisticas['Top_10s'] = estadisticas['Top_10s'].astype(int)


rid = rider
temp = st.sidebar.selectbox('SELECT SEASON', uniqueSeason, 17)


col1, col2 = st.columns([3, 2])


with col1:
    st.subheader("ALL THE CYCLIST & SEASONS")
    st.dataframe(estadisticas)




# Rider_Name,Season,Points,Racedays,KMs_Rode,Wins,Top_10s

porcorredortemporadas = estadisticas.loc[estadisticas['Rider_Name'].str.contains(str(rid), case=False)]


porcorredortemporadas['Season'] = porcorredortemporadas['Season'].astype(int)
porcorredortemporadas['Points'] = porcorredortemporadas['Points'].astype(int)
porcorredortemporadas['Racedays'] = porcorredortemporadas['Racedays'].astype(int)
porcorredortemporadas['KMs_Rode'] = porcorredortemporadas['KMs_Rode'].astype(int)
porcorredortemporadas['Wins'] = porcorredortemporadas['Wins'].astype(int)
porcorredortemporadas['Top_10s'] = porcorredortemporadas['Top_10s'].astype(int)

with col2:
    st.subheader("BEST 40 " + str(int(temp)).upper())
    corredoresunatemporadas = estadisticas[estadisticas['Season']==temp]
    corredoresunatemporadas = corredoresunatemporadas.rename(columns={'Rider_Name': 'index'}).set_index('index')
    corredoresunatemporadas = corredoresunatemporadas.sort_values(by='Points', ascending=False)
    corredoresunatemporadas= corredoresunatemporadas.head(40)
    chart_data = pd.DataFrame(corredoresunatemporadas, columns=['Points'])
    st.bar_chart(chart_data)


with col1:
    st.subheader(" CYCLIST " + str(rid).upper())
    st.dataframe(porcorredortemporadas)
with col2:
    st.subheader("POINTS / SEASON " + str(rid).upper())

    porcorredortemporadas = porcorredortemporadas.rename(columns={'Season': 'index'}).set_index('index')

    #chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])

    chart_data = pd.DataFrame(porcorredortemporadas,columns=['Points'])
    chart_data2 = pd.DataFrame(porcorredortemporadas,columns=['Points'])

    st.line_chart(chart_data)
    #st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)






st.subheader("TOP " + str(number_cyclist_selected) +" CYCLIST IN: " + str(int(temp)).upper())

corredoresunatemporadas2 = estadisticas[estadisticas['Season']==temp]
corredoresunatemporadas2 = corredoresunatemporadas2.sort_values(by='Points', ascending=False)
corredoresunatemporadas2= corredoresunatemporadas2.head(number_cyclist_selected)


c = alt.Chart(corredoresunatemporadas2).mark_circle().encode( x='Points' , y='Top_10s', size='Wins', color='Rider_Name', tooltip=['Rider_Name','Points', 'Top_10s', 'Wins'])

f = alt.Chart(corredoresunatemporadas2).mark_circle( size= 25).encode( x='Points' , y='Top_10s', color='Rider_Name', tooltip=['Wins', 'Rider_Name','Points', 'Top_10s' ])

st.altair_chart(c, use_container_width=True)

st.altair_chart(f, use_container_width=True)

#URLs = pd.read_csv('RiderProfile_URLs.csv',index_col=0)
#st.dataframe(URLs)

#Race_Name,Name,Season,Age,Rank,Team_Name,UCI,Finishing_Time
st.header("ANÁLISIS POR EQUIPOS EN "+ str(int(temp)) )
st.dataframe(competitionsstats)

#FILTRAMOS EL EQUIPO -> POR AÑO
equipos_year = competitionsstats.loc[competitionsstats['Season']==temp]
st.dataframe(equipos_year)

#Race_Name,Name,Season,Age,Rank,Team_Name,UCI,Finishing_Time
#paris-roubaix,dylan-van-baarle,2022,29,1,ineos-grenadiers-2022,500,5:37:00

equipos_edad = equipos_year[['Team_Name','Age']]

# COMBOBOX - TEAMS
teams = rcController.get_dataframe_teams(str(season))
team = st.sidebar.selectbox('SELECT A TEAM', teams)

# DATAFRAME - TEAM SEASON
team_season = rcController.get_dataframe_race_results_classics_team_season(team,str(season))
st.bar_chart(team_season)




# EDAD MEDIA
equipos_edad = equipos_edad[['Team_Name']].mean()
equipos_year = equipos_year[['Team_Name', 'UCI']]

# PUNTOS EN CLÁSICAS
equipos_puntos = equipos_year.groupby(['Team_Name']).sum()
equipos_puntos  = equipos_puntos .sort_values('Team_Name', ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

st.dataframe(equipos_puntos)
st.bar_chart(equipos_puntos)

# LEFT JOIN WITH PANDAS
df_puntos_edadmedia_clasicas = equipos_edad

df_puntos_edadmedia_clasicas.merge(equipos_puntos, on='Team_Name', how='left')


st.dataframe(df_puntos_edadmedia_clasicas)

# REPRESENTAMOS GRAFICOS


data_top2 = competitionsstats.head()

filter_rider = st.sidebar.selectbox()

cols_to_check = ['Race_Name','Name','Season','Age','Rank','Team_Name','UCI','Finishing_Time']


