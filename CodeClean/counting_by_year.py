import pandas as pd

competitionsstats2 = pd.read_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\Url_Races_winner_10_Years_Category_WT.csv', header=0)

#year,race_id,winner_id,category

df = competitionsstats2.groupby(['year','winner_id'])['race_id'].count()

df = df.reset_index()

medals = df.pivot_table('race_id', ['winner_id'], 'year')
print(medals)
medals = medals.reset_index()
medals = medals.fillna(0)
print(medals)


medals.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\export_groupandcount.csv', index=False, header=True)


print(medals)