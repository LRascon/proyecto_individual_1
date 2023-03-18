from fastapi import FastAPI
from typing import Optional
import pandas as pd

app = FastAPI()
app.title = "Proyecto Individual Nº1"

movies_df = pd.read_csv('./datasets/data_streaming.csv')

@app.get('/Info', tags=['Información'])
def message():
    return '¡Bienvenido!, estas son algunas de las consultas rápidas de interés.'

'''
Consulta 1:
Película con mayor duración con filtros opcionales de AÑO, 
PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration
(year, platform, duration_type))
'''

@app.get('/max_duration', tags=['Consultas'])
async def get_max_duration(year: Optional[int] = None,
                           platform: Optional[str] = None,
                           duration_type: Optional[str] = None):
    filtered_df = movies_df.copy()
    if year:
        filtered_df = filtered_df[filtered_df['release_year'] == year]
    if platform:
        filtered_df = filtered_df[filtered_df['platform'] == platform]
    if duration_type:
        filtered_df = filtered_df[filtered_df['duration_type'] == duration_type]
    max_duration = filtered_df['duration_int'].max()
    movie = filtered_df[filtered_df['duration_int'] == max_duration].iloc[0]['title']
    return {'movie': movie, 'max_duration': max_duration}

'''
Consulta 2:
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 
(la función debe llamarse get_score_count(platform, scored, year)
'''
@app.get("/score-count", tags=['Consultas'])
async def get_score_count(platform: str, scored: int, year: int):
    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("./datasets/data_streaming.csv")

    # Filtrar los datos por plataforma, puntuación y año
    filtered_df = df[(df["platform"] == platform) & (df["score"] >= scored) & (df["release_year"] == year)]

    # Contar la cantidad de películas encontradas
    count = filtered_df.shape[0]

    # Devolver la cantidad de películas encontradas
    return {"count": count}

'''
Consulta 3:
Cantidad de películas por plataforma con filtro de PLATAFORMA.
(La función debe llamarse get_count_platform(platform))
'''

@app.get("/count_platform", tags=['Consultas'])
async def get_count_platform(platform: str):
    movies_platform = movies_df[movies_df["platform"] == platform]
    movies_count = movies_platform["platform"].value_counts().to_dict()
    return movies_count

'''
Consulta 4:
Actor que más se repite según plataforma y año.
(La función debe llamarse get_actor(platform, year))
'''
@app.get("/actor", tags=['Consultas'])
async def get_actor(platform: str, year: int):
    # Filtrar el dataframe por plataforma y año
    df_filtered = movies_df[(movies_df['platform'] == platform) & (movies_df['release_year'] == year)]
    
    # Separar cada actor en una fila independiente
    df_cast = df_filtered.explode('cast')
    
    # Agrupar por actor y contar las repeticiones
    actor_count = df_cast.groupby('cast')['cast'].count()
    
    # Encontrar el actor más repetido
    actor_most_common = actor_count.idxmax()
    
    return {'actor': actor_most_common}