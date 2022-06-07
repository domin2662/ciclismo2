import numpy as np
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
riders_by_season = CyController.get_dataframe_all_cyclists_by_seson()
nationalities = CyController.get_dataframe_nationality()



###############TITULO##################
st.set_page_config(layout="wide")
st.image('bike.jpg')
###########  SIDEBAR MENU   ##########
st.sidebar.title(":bike:CIDEAM CYCLING")
#typeofcompetition = st.sidebar.radio("Type of Competition", ('climbing', 'general_classification', 'time_trial', 'sprint', 'one_day_races'))
typeofcompetition  = st.sidebar.multiselect( 'Types of Competitions', ('climbing', 'general_classification', 'time_trial', 'sprint', 'one_day_races'))
nationality = st.sidebar.selectbox('SELECT A RIDER', nationalities)
rider = st.sidebar.selectbox('SELECT A RIDER', profiles)
rider2 = st.sidebar.selectbox('SELECT A RIDER TO COMPARE', profiles)
#multirider = st.sidebar.multiselect('SELECT A RIDER', profiles)
number_cyclist_selected_historical = st.sidebar.slider("Number of cyclist history",1,30,15)
number_cyclist_selected = st.sidebar.slider("Number of cyclist",1,200,20)
season = st.sidebar.selectbox('SELECT A SEASON', seasons)

# COMBOBOX - TEAMS
teams = rcController.get_dataframe_teams(str(season))
team = st.sidebar.selectbox('SELECT A TEAM', teams)



##### OPTION WITH PANDAS #################
#result =profiles.loc[profiles[cols_to_check][0] == rider]
#result = profiles.loc[profiles['Rider_id'].str.contains(str(rider), case=False)]

################# CENTRAL MENU ########################
# FILTER RESULT WIT POSTGRES
col1,col2 = st.columns(2)
with col1:
    st.header(" 👨‍👨‍👦‍👦 ALL THE CYCLIST - HISTORICAL  👨‍👨‍👦‍👦")
    result= CyController.get_dataframe_cyclist(str(rider))
    st.dataframe(profiles)
    type = np.array(typeofcompetition)
    type=['id_cyclist']
    type.extend(typeofcompetition)

with col2:
    st.header(" 👨‍👨‍👦‍👦 ALL THE CYCLIST  FROM "+str(nationality).upper())
    result = CyController.get_dataframe_cyclist(str(rider))
    porcorredortemporadas = riders_by_season.loc[riders_by_season['id_cyclist'].str.contains(str(rider), case=False)]

    profiles_by_nationality = profiles.loc[profiles['nationality'].str.contains(str(nationality), case=False)]
    st.dataframe(profiles_by_nationality )
    type = np.array(typeofcompetition)
    type = ['id_cyclist']
    type.extend(typeofcompetition)


#### DYNAMIC FILTER ###########
if(len(typeofcompetition)>0):
    filter_by_competition = profiles[type].sort_values(by=str(type[0]),ascending=False)
    filter_by_competition  = filter_by_competition[:number_cyclist_selected_historical]
    #st.dataframe(filter_by_competition)
    #filter_by_competition = filter_by_competition.astype(str)
    #st.subheader("THE BEST "+ str(number_cyclist_selected) +" CYCLISTS IN " +str(typeofcompetition).upper())
    st.subheader("THE BEST "+ str(number_cyclist_selected) +" CYCLISTS " )
    chart_data_discipline= filter_by_competition.rename(columns={'id_cyclist': 'index'}).set_index('index')
    st.bar_chart(chart_data_discipline)

st.markdown('##')
#4 COLUMNS
col1,col2,col3 = st.columns(3)
with col1:
    st.text('➕ COMBINE ')
    filter_by_competition_combine = profiles[['id_cyclist','climbing','sprint','general_classification','time_trial','one_day_races'  ]].sort_values(by=str('climbing'),ascending=False)
    filter_by_competition_combine = filter_by_competition_combine[:number_cyclist_selected]
    chart_data_discipline_combine = filter_by_competition_combine.rename(columns={'id_cyclist': 'index','general_classification':'GC', 'one_day_races':'ONE DAY'  }).set_index('index')


    st.bar_chart(chart_data_discipline_combine)

with col2:
    st.text('💨 SPRINT ')
    filter_by_competition_sprint = profiles[['id_cyclist','sprint']].sort_values(by=str('sprint'),ascending=False)
    filter_by_competition_sprint = filter_by_competition_sprint[:number_cyclist_selected_historical]
    chart_data_discipline_sprint = filter_by_competition_sprint.rename(columns={'id_cyclist': 'index','sprint':'SP' }).set_index('index')
    st.bar_chart(chart_data_discipline_sprint)

with col3:
    st.text('📈 GENERAL ')
    filter_by_competition_general_classification = profiles[['id_cyclist','general_classification']].sort_values(by=str('general_classification'),ascending=False)
    filter_by_competition_general_classification = filter_by_competition_general_classification[:number_cyclist_selected_historical]
    chart_data_discipline_general_classification = filter_by_competition_general_classification.rename(columns={'id_cyclist': 'index','general_classification':'GC' }).set_index('index')
    st.bar_chart(chart_data_discipline_general_classification)

col1,col2,col3= st.columns(3)
st.markdown('##')

with col1:
    st.text ('⏲️TT')
    filter_by_competition_time_trial = profiles[['id_cyclist','time_trial']].sort_values(by=str('time_trial'),ascending=False)
    filter_by_competition_time_trial = filter_by_competition_time_trial[:number_cyclist_selected_historical]
    chart_data_discipline_time_trial = filter_by_competition_time_trial.rename(columns={'id_cyclist': 'index','time_trial': 'TT' }).set_index('index')
    st.bar_chart(chart_data_discipline_time_trial)

with col2:
    st.text('📐 ONE DAY')
    filter_by_competition_one_day_races = profiles[['id_cyclist','one_day_races']].sort_values(by=str('one_day_races'),ascending=False)
    filter_by_competition_one_day_races = filter_by_competition_one_day_races[:number_cyclist_selected_historical]
    chart_data_discipline_one_day_races = filter_by_competition_one_day_races.rename(columns={'id_cyclist': 'index','one_day_races':'ONEDAY' }).set_index('index')
    st.bar_chart(chart_data_discipline_one_day_races)
with col3:
    st.text('📐 CLIMBING')
    filter_by_competition_climbing = profiles[['id_cyclist', 'climbing']].sort_values(by=str('climbing'),                                                                                  ascending=False)
    filter_by_competition_climbing = filter_by_competition_climbing[:number_cyclist_selected_historical]
    chart_data_discipline_climbing = filter_by_competition_climbing.rename(columns={'id_cyclist': 'index','climbing':'MNT'}).set_index('index')
    st.bar_chart(chart_data_discipline_climbing)



# AgGrid(profiles)

col1, col2 = st.columns([3, 2])

################# SELECTED RIDER ########################
result= CyController.get_dataframe_cyclist(str(rider))
porcorredortemporadas = riders_by_season.loc[riders_by_season['id_cyclist'].str.contains(str(rider), case=False)]


#######  HEADING  #######
st.markdown('##')
st.header(' 🙋‍♂️  SELECTED RIDER   ‍♂🙋️')

col1, col2, col3 = st.columns(3)



with col1:
    st.subheader("SELECTED : " + str(rider).upper())
    st.dataframe(result)
    st.write(" ")
    st.write("🙋‍♂ NAME :  " + str(result.iat[0,1]).upper())
    st.write("🗺️ NATION :  " + str(result.iat[0,3]).upper())
    st.write("🔴 WEIGHT :  " + str(result.iat[0,2]).upper())
    st.write("👆 HEIGHT :  " + str(result.iat[0,9]).upper())
    st.markdown('####')
    st.markdown('####')
    st.markdown('#')


with col2:
    st.subheader("POINTS/S " + str(rider).upper())
    porcorredortemporadaspoints = porcorredortemporadas.rename(columns={'season': 'index'}).set_index('index')

    # chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])

    chart_data_points = pd.DataFrame(porcorredortemporadaspoints, columns=['point'])
    chart_data2_points = pd.DataFrame(porcorredortemporadaspoints, columns=['point'])

    st.line_chart(chart_data_points)
    # st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)
    st.markdown('####')
    st.markdown('###')

#### GENERATE A RADAR ###############
with col3:
    st.subheader("RADAR : " + str(rider).upper())

    option = {
        "radar": {
            "indicator": [
                {"name": "CLIMBER", "max": 19014},
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
                        "value": [int(result.iat[0,6]), int(result.iat[0,4]), int(result.iat[0,5]), int(result.iat[0,7]), int(result.iat[0,8])],
                        "name": "预算分配（Allocated Budget）",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="350px")

with col1:
    st.subheader("WINS/S " + str(rider).upper())
    porcorredortemporadas_wins = porcorredortemporadas.rename(columns={'season': 'index'}).set_index('index')

    # chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])

    chart_data_wins = pd.DataFrame(porcorredortemporadas_wins, columns=['wins'])
    #chart_data2 = pd.DataFrame(porcorredortemporadas, columns=['wins'])

    st.line_chart(chart_data_wins)
    # st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)

with col2:
    st.subheader("TOP_TEN/S " + str(rider).upper())
    porcorredortemporadas_toptens = porcorredortemporadas.rename(columns={'season': 'index'}).set_index('index')

    # chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])

    chart_data_toptens = pd.DataFrame(porcorredortemporadas_toptens, columns=['toptens'])


    st.line_chart(chart_data_toptens)
    # st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)

#### GENERATE A RADAR ###############
with col3:
    st.subheader("DAYS : " + str(rider).upper())
    porcorredortemporadas_race_days = porcorredortemporadas.rename(columns={'season': 'index'}).set_index('index')

    # chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])

    chart_data_race_days = pd.DataFrame(porcorredortemporadas_race_days, columns=['racedays'])

    st.line_chart(chart_data_race_days)
    # st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)

#######HEADING ##############
st.markdown('##')
st.header(' 🙋‍♂️ COMPARE TWO RIDERS  🙋‍♂️')


################# COMPARE TWO RIDERS NOT IMPLEMENTED ########################

# result_first_rider= CyController.get_dataframe_cyclist(str(rider))
# porcorredortemporadas_first_rider = riders_by_season.loc[riders_by_season['id_cyclist'].str.contains(str(rider), case=False)]
# resutl_second_rider=  CyController.get_dataframe_cyclist(str(rider2))
# porcorredortemporadas_second_rider = riders_by_season.loc[riders_by_season['id_cyclist'].str.contains(str(rider2), case=False)]
#
# st.write(porcorredortemporadas_first_rider )
# st.write(porcorredortemporadas_second_rider)
#
#
# frames =[porcorredortemporadas_first_rider,porcorredortemporadas_second_rider]
# result_to_compare = pd.concat(frames, keys=["id_cyclist", "season", "point","racedays","kms_rode","wins","toptens"])
#
# result_to_compare  = result_to_compare.rename(columns={'season': 'index'}).set_index('index')
#
# st.write(result_to_compare)
#
# # chart_data = pd.DataFrame(porcorredortemporadas, columns=['Points', 'Racedays', 'KMs_Rode', 'Wins', 'Top_10s'])
#
# chart_data_points_compare = pd.DataFrame(result_to_compare, columns=['id_cyclist'])
# st.write(chart_data_points_compare )
# st.area_chart(chart_data_points_compare )
# # st.line_chart(porcorredortemporada, width=0, height=0, use_container_width=True)
# st.markdown('####')
# st.markdown('###')




################## WORKING WITH PANDAS NOT IMPLEMENTED #########################

# uniqueId = estadisticas["Rider_Name"].unique()
# uniqueSeason = estadisticas["Season"].unique()
# estadisticas['Season'] = estadisticas['Season'].astype(int)
# estadisticas['Points'] = estadisticas['Points'].astype(int)
# estadisticas['Racedays'] = estadisticas['Racedays'].astype(int)
# estadisticas['KMs_Rode'] = estadisticas['KMs_Rode'].astype(int)
# estadisticas['Wins'] = estadisticas['Wins'].astype(int)
# estadisticas['Top_10s'] = estadisticas['Top_10s'].astype(int)




#temp = st.sidebar.selectbox('SELECT SEASON', uniqueSeason, 17)
st.markdown('##')
st.header(' 📆️ SEASON DATA   📆️ : '+ str(season) )

col1, col2 = st.columns(2)

# Rider_Name,Season,Points,Racedays,KMs_Rode,Wins,Top_10s

# porcorredortemporadas['Season'] = porcorredortemporadas['Season'].astype(int)
# porcorredortemporadas['Points'] = porcorredortemporadas['Points'].astype(int)
# porcorredortemporadas['Racedays'] = porcorredortemporadas['Racedays'].astype(int)
# porcorredortemporadas['KMs_Rode'] = porcorredortemporadas['KMs_Rode'].astype(int)
# porcorredortemporadas['Wins'] = porcorredortemporadas['Wins'].astype(int)
# porcorredortemporadas['Top_10s'] = porcorredortemporadas['Top_10s'].astype(int)

with col1:
    st.subheader("ALL THE CYCLIST & SEASONS")
    st.dataframe(riders_by_season)



with col2:
    st.subheader("BEST 40 " + str(int(season)).upper())
    corredoresunatemporadas = riders_by_season[riders_by_season['season']==season]
    corredoresunatemporadas = corredoresunatemporadas.rename(columns={'id_cyclist': 'index'}).set_index('index')
    corredoresunatemporadas = corredoresunatemporadas.sort_values(by='point', ascending=False)
    corredoresunatemporadas= corredoresunatemporadas.head(40)
    chart_data = pd.DataFrame(corredoresunatemporadas, columns=['point'])
    st.bar_chart(chart_data)

############## NOT IMPLEMENTED ########################

# with col1:
#     st.subheader(" CYCLIST " + str(rider).upper())
#     st.dataframe(porcorredortemporadas)







st.subheader("TOP " + str(number_cyclist_selected) +" CYCLIST IN: " + str(int(season)).upper())

corredoresunatemporadas2 = riders_by_season[riders_by_season['season']==season]
corredoresunatemporadas2 = corredoresunatemporadas2.sort_values(by='point', ascending=False)
corredoresunatemporadas2= corredoresunatemporadas2.head(number_cyclist_selected)


c = alt.Chart(corredoresunatemporadas2).mark_circle().encode( x='point' , y='toptens', size='wins', color='id_cyclist', tooltip=['id_cyclist','point', 'toptens', 'wins'])

f = alt.Chart(corredoresunatemporadas2).mark_circle(size= 25).encode( x='point' , y='toptens', color='id_cyclist', tooltip=['wins', 'id_cyclist','point', 'toptens' ])

st.altair_chart(c, use_container_width=True)

st.subheader("TOP - NON FILTER WINS" + str(number_cyclist_selected) +" CYCLIST IN: " + str(int(season)).upper())

st.altair_chart(f, use_container_width=True)

#URLs = pd.read_csv('RiderProfile_URLs.csv',index_col=0)
#st.dataframe(URLs)

#Race_Name,Name,Season,Age,Rank,Team_Name,UCI,Finishing_Time
st.header("👨‍👨‍👦‍👦 RESULTADOS HISTÓRICOS DE CLÁSICAS" )
st.dataframe(competitionsstats)

#FILTRAMOS EL EQUIPO -> POR AÑO
st.header("👨‍👨‍👦‍👦 ANÁLISIS POR EQUIPOS EN "+ str(int(season)) )
equipos_year = competitionsstats.loc[competitionsstats['Season']== season]
st.dataframe(equipos_year)

#Race_Name,Name,Season,Age,Rank,Team_Name,UCI,Finishing_Time
#paris-roubaix,dylan-van-baarle,2022,29,1,ineos-grenadiers-2022,500,5:37:00

equipos_edad = equipos_year[['Team_Name','Age']]


# DATAFRAME - TEAM SEASON
teams = rcController.get_dataframe_teams(str(season))
team_season = rcController.get_dataframe_race_results_classics_team_season(team)

team_by_rider = team_season.groupby(['id_cyclist']).sum()

st.dataframe(team_season)
st.dataframe(team_by_rider.sort_values(['uci'],False))
st.bar_chart(team_by_rider)



by_rider = {
    "legend": {"top": "bottom"},
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "restore": {"show": True},
            "saveAsImage": {"show": True},
        },
    },
    "series": [
        {
            "name": "面积模式",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 10},
            "data": [
                {"value": 40, "name": "rose 1"},
                {"value": 38, "name": "rose 2"},
                {"value": 32, "name": "rose 3"},
                {"value": 30, "name": "rose 4"},
                {"value": 28, "name": "rose 5"},
                {"value": 26, "name": "rose 6"},
                {"value": 22, "name": "rose 7"},
                {"value": 18, "name": "rose 8"},
                {"value": 18, "name": "rose 9"},
                {"value": 18, "name": "rose 10"},
            ],
        }
    ],
}
st_echarts(
    options=by_rider, height="600px",
)



# EDAD MEDIA
equipos_edad = equipos_edad[['Team_Name']].mean()
equipos_year = equipos_year[['Team_Name', 'UCI']]

# PUNTOS EN CLÁSICAS
equipos_puntos = equipos_year.groupby(['Team_Name']).sum()
equipos_puntos  = equipos_puntos .sort_values('Team_Name', ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

st.dataframe(equipos_puntos)
st.bar_chart(equipos_puntos)



by_rider = {
    "legend": {"top": "bottom"},
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "restore": {"show": True},
            "saveAsImage": {"show": True},
        },
    },
    "series": [
        {
            "name": "面积模式",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 10},
            "data": [
                {"value": 40, "name": "rose 1"},
                {"value": 38, "name": "rose 2"},
                {"value": 32, "name": "rose 3"},
                {"value": 30, "name": "rose 4"},
                {"value": 28, "name": "rose 5"},
                {"value": 26, "name": "rose 6"},
                {"value": 22, "name": "rose 7"},
                {"value": 18, "name": "rose 8"},
                {"value": 18, "name": "rose 9"},
                {"value": 18, "name": "rose 10"},
            ],
        }
    ],
}
st_echarts(
    options=by_rider, height="600px",
)



# LEFT JOIN WITH PANDAS
#df_puntos_edadmedia_clasicas = equipos_edad

#df_puntos_edadmedia_clasicas.merge(equipos_puntos, on='Team_Name', how='left')


#st.dataframe(df_puntos_edadmedia_clasicas)

# REPRESENTAMOS GRAFICOS


#data_top2 = competitionsstats.head()



#cols_to_check = ['Race_Name','Name','Season','Age','Rank','Team_Name','UCI','Finishing_Time']


