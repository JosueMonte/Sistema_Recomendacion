from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()


@app.get('/')
def read_root():
    return {"welcome": "Bienvenido a la API"}


@app.get('/cantidad_filmaciones_mes')
def cantidad_filmaciones_mes(mes: str):
    return {"endpoint1": f"Fueron estrenadas 1000 peliculas en el mes de {mes}"}


@app.get('/cantidad_filmaciones_dia')
def cantidad_filmaciones_dia(dia: str):
    return {"endpoint2": f"Fueron estrenadas 1000 peliculas los días {dia}"}


@app.get('/score_titulo')
def score_titulo(titulo: str):
    return {"endpoint3": f"La película {titulo} fue estrenada en el año 1000 con un puntaje de 100"}


@app.get('/votos_titulo')
def votos_titulo(titulo: str):
    return {"endpoint4": f"La película {titulo} fue estrenada en el año Y, cuenta con un total de Y valoraciones y un promedio de Z"}


@app.get('/get_actor')
def get_actor(nombre_actor: str):
    return {"endpoint5": f"El actor {nombre_actor} ha participado de Y cantidad de filmaciones, ha conseguido un retorno de Y y un promedio de retorno de X por filmación"}


@app.get('/get_director')
def get_director(nombre_director: str):
    return {"endpoint6": f"El director {nombre_director} ha conseguido un retorno de Y, y sus películas con su respectiva fecha de lanzamiento, retorno individual, costo y ganancia son las siguientes:"}


@app.get('/recomendacion')
def recomendacion(titulo: str):
    return {'endpoints7': f'Te recomiendo mirar estas películas similares:',
            'lista de películas:': ['película1',
                                    'película2',
                                    'película3',
                                    'película4',
                                    'película5']}


# Cargar el DataFrame
df = pd.read_csv('data_movies.csv')

# Mapeo de meses
month_mapping = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}


@app.get('film_count_m')
def film_count_m(month: str):
    # Convertir el nombre del mes a su número correspondiente
    month_number = month_mapping.get(month.lower())
    if month_number is None:
        raise ValueError(f"Mes '{month}' no es válido.")

    # Filtrar las filas que corresponden al mes especificado
    filtered_df = df[df['month'] == month_number]
    # Contar los IDs en las filas filtradas
    count_ids = filtered_df['id'].count()
    return {"endpoint0": f"Fueron estrenadas {count_ids} peliculas en el mes de {month}"}
