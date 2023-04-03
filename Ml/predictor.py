'''
1. Importa las bibliotecas necesarias:
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def convert_to_int(value):
    try:
        int_value = int(value)
        if int_value == float(value):
            return int_value
        else:
            return value
    except (ValueError, TypeError):
        return value

'''
2. Carga los archivos CSV:
'''
carreras_df = pd.read_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\resultadoscon2023.csv')
info_carreras_df =pd.read_csv(r'C:\Users\DOMIN2662\Documents\GitHub\ciclismo2\BBDDcsv\leaderboard.csv')
'''
3. Filtra la columna "Rank" manteniendo solo los valores de tipo integer y float:
'''


# Convierte la columna de fecha en un objeto de fecha
carreras_df['DATE'] = pd.to_datetime(carreras_df['DATE'], format='%d %B %Y')

# Crea un diccionario de mapeo de mes a temporada
seasons = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'}

# Usa el atributo .dt para obtener el mes de cada fecha y mapear a la temporada correspondiente
carreras_df['seasons'] = carreras_df['DATE'].dt.month.map(seasons)

carreras_df['DATE'] = pd.to_datetime(carreras_df['DATE'], format='%d %B %Y')

print(carreras_df.head())

# Añade la columna "año" con el año de cada fecha
carreras_df['Season'] = carreras_df['DATE'].dt.year


'''
3. Combina ambos DataFrames en uno solo utilizando Race_Name como clave:
'''
df = pd.merge(carreras_df, info_carreras_df, on=['Race_Name','Season'])

'''
3. Filtra la columna "Rank" manteniendo solo los valores de tipo integer y float:
'''

df['Rank'] = df['Rank'].apply(convert_to_int)

df = df.loc[df['Rank'].apply(lambda x: isinstance(x, int))]

df['Rank'] = df['Rank'].astype(int)

df['Points_scale'] = df['Points_scale'].astype(int)
df['Uci_scale'] = df['Uci_scale'].astype(int)

print(df.dtypes)

print(df.head())


'''
3. Filtra la columna "Rank" manteniendo solo los valores de tipo integer y float:
'''





'''
4. Prepara los datos para el entrenamiento:
'''
# Filtra solo las columnas relevantes
X = df[['Season', 'Age', 'Rank', 'Race_ranking', 'Start_list_quality_score', 'Uci_scale', 'Points_scale']]
y = df['Name']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Estandariza los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
'''
5. Entrena un modelo de clasificación (en este caso, RandomForest):
'''
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
'''

6. Evalúa la precisión del modelo:
python'''
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy}')

'''
7. Predecir el ganador para el próximo año:
'''
next_year = df[df['Season'] == max(df['Season'])+1]
next_year_X = next_year[['Age', 'Rank', 'Race_ranking', 'Start_list_quality_score', 'Uci_scale', 'Points_scale']]
next_year_X_scaled = scaler.transform(next_year_X)
next_year_pred = clf.predict(next_year_X_scaled)


print(f'El ganador predicho para el próximo año es: {next_year_pred[0]}')

'''
Ten en cuenta que este es un ejemplo básico y hay muchas maneras de mejorar la precisión del modelo, como ajustar los hiperparámetros del algoritmo, probar diferentes algoritmos de clasificación, o realizar ingeniería de características en los datos.

continua ampliando el modelo e indicame los 10 corredores con más p
Para obtener los 10 corredores con más posibilidades de ganar la carrera, puedes utilizar la función `predict_proba` para obtener las probabilidades de cada clase y luego ordenar los resultados. Aquí tienes cómo hacerlo:

8. Obtén las probabilidades de cada corredor y selecciona los 10 corredores con más posibilidades:
'''

next_year_prob = clf.predict_proba(next_year_X_scaled)
prob_df = pd.DataFrame(next_year_prob, columns=clf.classes_)
prob_df['Name'] = next_year['Name'].reset_index(drop=True)

# Ordena los corredores por la probabilidad más alta y selecciona los 10 primeros
top_10 = prob_df.nlargest(10, prob_df.columns[0])[['Name']]

print('Los 10 corredores con más posibilidades de ganar la carrera son:')
print(top_10)

'''
Esto te dará un DataFrame con los 10 corredores que tienen más posibilidades de ganar la carrera según el modelo. Ten en cuenta que la precisión del modelo puede no ser alta, por lo que es importante seguir mejorando y ajustando el modelo como se mencionó anteriormente.
'''