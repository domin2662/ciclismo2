
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
'''
2. Carga los archivos CSV:
'''
info_carreras_df =pd.read_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\leaderboard.csv')
'''
3. Filtra la columna "Rank" manteniendo solo los valores de tipo integer y float:
'''
def convert_to_int(value):
    try:
        int_value = int(value)
        if int_value == float(value):
            return int_value
        else:
            return value
    except (ValueError, TypeError):
        return value

# Convertir valores que puedan ser enteros en int en la columna 'columna'


'''
3. Combina ambos DataFrames en uno solo utilizando Race_Name como clave:
'''
df = info_carreras_df

df['Rank'] = df['Rank'].apply(convert_to_int)
print(df.head())
print(df.dtypes)
df = df.loc[df['Rank'].apply(lambda x: isinstance(x, int))]
print(df.head())

df.to_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\soloint.csv', index=False, header=True)
