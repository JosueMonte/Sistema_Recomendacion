from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()


@app.get('/')
def read_root():
    return {"welcome": "Bienvenido a la API"}


# Mapeo de meses
month_mapping = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}


def cantidad_filmaciones_mes(df, month: str):
    """Obtiene la cantidad de filmaciones según mes indicado
    Args:
        df: DataFrame de películas 
        month (str): nombre del mes en castellano
    Raises:
        HTTPException: en caso de que el mes indicado no sea válido o no esté escrito en castellano o sea nulo
    Returns:
        _type_: entero o integer
    """
    # Convertir el nombre del mes a su número correspondiente
    month_number = month_mapping.get(month.lower())
    if month_number is None:
        raise HTTPException(
            status_code=400, detail=f"Mes '{month}' no es válido.")
    # Filtrar las filas que corresponden al mes especificado
    df_filter_month = df[df['month'] == month_number]
    # Contar los IDs en las filas filtradas
    count_ids = df_filter_month['id'].count()
    return {"endpoint1": f"Fueron estrenadas {count_ids} peliculas en el mes de {month}"}


@app.get('/cantidad_filmaciones_mes/{month}')
async def film_cant_mes(month: str):
    """Obtiene la cantidad de filmaciones según mes desde un archivo en formato csv
    Args:
        month (str): ejemplo: "enero"
    Returns:
        _type_: ejemplo: Fueron estrenadas 2000 películas en el mes de enero
    """
    try:
        # Busca la ruta del archivo y crea el DataFrame como variable
        df = pd.read_csv("dataset/data_movies.csv")
        # Aplicar la función para obtener la cantidad de filmaciones según mes aplicado
        result = cantidad_filmaciones_mes(df, month)
        return JSONResponse(content=jsonable_encoder(result), media_type="application/json")
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail="Archivo csv no encontrado, revisa si la ruta del archivo es correcta.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}")


def cantidad_filmaciones_dia(df, weekday: str):
    """Obtiene la cantidad de filmaciones según día de la semana indicado
    Args:
        df: DataFrame de películas 
        weekday (str): nombre del día de la semana en castellano
    Raises:
        HTTPException: en caso de que el día de la semana indicado no sea válido o no esté escrito en castellano o sea nulo
    Returns:
        _type_: entero o integer
    """
    # Lista de días válidos en castellano
    dias_validos = ['lunes', 'martes', 'miércoles',
                    'jueves', 'viernes', 'sábado', 'domingo']
    if weekday not in dias_validos:
        raise HTTPException(
            status_code=400, detail=f"El día '{weekday}' no es válido.")
    # Filtrar las filas que corresponden al dia de la semana especificado
    df_filter_day = df[df['weekday'] == weekday]
    # Contar los IDs en las filas filtradas
    count_ids = df_filter_day['id'].count()
    return {"endpoint2": f"Fueron estrenadas {count_ids} peliculas los dias {weekday}"}


@app.get('/cantidad_filmaciones_dia/{weekday}')
async def film_cant_dia(weekday: str):
    """Obtiene la cantidad de filmaciones según dia de la semana desde un archivo en formato csv
    Args:
        weekday (str): ejemplo: "lunes"
    Returns:
        _type_: ejemplo: Fueron estrenadas 2000 películas los dias lunes
    """
    try:
        # Busca la ruta del archivo y crea el DataFrame como variable
        df = pd.read_csv("dataset/data_movies.csv")
        # Aplicar la función para obtener la cantidad de filmaciones según dia de semana aplicado
        result = cantidad_filmaciones_dia(df, weekday)
        return JSONResponse(content=jsonable_encoder(result), media_type="application/json")
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail="Archivo csv no encontrado, revisa si la ruta del archivo es correcta.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}")


def score_titulo(df, titulo: str):
    """Obtiene el año de estreno y la popularidad de la película y dataset ingresados

    Args:
        df: DataFrame de películas
        titulo (str): nombre de la película
    Raises:
        HTTPException: en caso de que la película no esté escrita de forma correcta o no esté ingresada en el dataset o es inexistente.
    Returns:
        _type_: str
    """
    # Verificar si el título de la película está en el DataFrame
    if titulo not in df['title'].values:
        raise HTTPException(
            status_code=400, detail=f"La película '{titulo}' no ha sido estrenada o no está registrada en el dataset o es inexistente.")

    # Filtrar la fila que corresponde a la película especificada
    pelicula = df[df['title'] == titulo]

    # Extrar año de estreno y popularidad
    release_year = pelicula['release_year'].values[0]
    popularity = pelicula['popularity'].values[0]
    return {'endpoint3': f"La película {titulo} fue estrenada en el año {release_year} con una popularidad de {popularity} puntos"}


@app.get('/score_titulo/{titulo}')
async def film_score(titulo: str):
    """Obtiene el año de estreno y la popularidad de la película ingresada

    Args:
        titulo (str): ejemplo: 'Toy Story'
    Returns:
        _type: ejemplo: La película 'Toy Story' fue estrenada en el año 1995 con una popularidad de 21.95 puntos    """

    try:
        # Busca la ruta del archivo en GitHub y crea el DataFrame como variable
        df = pd.read_csv('dataset/data_movies.csv')
        # Aplicar la función para obtener el año y la popularidad de la película ingresada
        result = score_titulo(df, titulo)
        return JSONResponse(content=jsonable_encoder(result), media_type='application/json')
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail='Archivo .csv no encontrado, revisa si la ruta del archivo es correcta.')
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}.")


def votos_titulo(df, titulo: str):
    """Obtiene el año de estreno, un total de valoraciones y un promedio según película ingresada
    Args:
        df: DataFrame de películas
        titulo (str): nombre de la película
    Raises:
        HTTPException: en caso de que la película no esté escrita de forma correcta, no esté ingresada en el dataset o sea inexistente. Además, debe contar con al menos 2000 valoraciones.
    Returns:
        dict: Contiene el año de estreno, total de valoraciones y el promedio de valoraciones.
    """

    # Verificar si el título de la película está en el DataFrame
    if titulo not in df['title'].values:
        raise HTTPException(
            status_code=400, detail=f"Puede ser que la película '{titulo}': no haya sido estrenada, no esté registrada en el dataset, sea inexistente o no cuente con un mínimo de 2000 valoraciones.")

    # Filtrar la fila que corresponde a la película especificada
    pelicula = df[df['title'] == titulo]

    # Extrar año de estreno y popularidad
    release_year = pelicula['release_year'].values[0]
    vote_count = pelicula['vote_count'].values[0]
    vote_average = pelicula['vote_average'].values[0]

    if vote_count < 2000:
        return {'endpoint4': f"La película {titulo} no cuenta con un mínimo de 2000 valoraciones y por tanto no se devuelve ningún valor."}

    return {'endpoint4': f"La película {titulo} fue estrenada en el año {release_year}, cuenta con un total de {vote_count} valoraciones y un promedio de {vote_average} puntos."}


@app.get('/votos_titulo/{titulo}')
async def film_vote(titulo: str):
    """Obtiene el año de estreno, la cantidad de votos y su promedio según película ingresada
    Args:
        titulo (str): ejemplo: 'Toy Story'
    Returns:
        _dict: ejemplo: La película 'Toy Story' fue estrenada en el año 1995, cuenta con un total de 5415 y un promedio de 7.7 puntos.
    """

    try:
        # Busca la ruta del archivo en GitHub y crea el DataFrame como variable
        df = pd.read_csv('dataset/data_movies.csv')
        # Aplicar la función para obtener el año, la cantidad de voto y el promedio de la película ingresada
        result = votos_titulo(df, titulo)
        return JSONResponse(content=jsonable_encoder(result), media_type='application/json')
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail='Archivo .csv no encontrado, revisa si la ruta del archivo es correcta.')
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}.")


def recomendacion(df, titulo: str):
    """Obtiene una lista de las 5 películas más similares a la ingresada por el usuario
    Args:
        df: DataFrame de películas
        titulo (str): nombre de la película
    Raises:
        HTTPException: en caso de que la película no esté escrita de forma correcta, no esté ingresada en el dataset o sea inexistente.
    Returns:
        dict: contiene una lista con los nombres de 5 películas.
    """

    # Verificar si el título de la película está en el DataFrame
    if titulo not in df['title'].values:
        raise HTTPException(
            status_code=400, detail=f"Puede ser que la película '{titulo}': no haya sido estrenada, no esté registrada en el dataset o sea inexistente.")

    # Vectorizar la columna 'title' usando TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['title'])

    # Codificar la columna 'genres_name' y 'studios_name' usando MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    genres_encoded = mlb.fit_transform(df['genres_name'])
    studios_encoded = mlb.fit_transform(df['studios_name'])

    # Luego, vamos a añadir las columnas numéricas y la matriz de géneros a nuestra matriz de características
    features = np.column_stack([tfidf_matrix.toarray(),
                                df['budget'],
                                df['vote_average'],
                                df['popularity'],
                                df['release_year'],
                                genres_encoded,
                                studios_encoded])

    # Reindexamos el DataFrame
    data = df.reset_index(drop=True)

    # Ahora, calculamos la matriz de similitud de coseno
    similarity_matrix = cosine_similarity(features)

    # Para hacer recomendaciones, puedes buscar las películas más similares a una película dada
    name_films = data[data['title'] == titulo]

    if not name_films.empty:
        product_index = name_films.index[0]
        product_similarities = similarity_matrix[product_index]

        # Se obtienen los índices de las 5 películas más similares (ordenados de forma descendente), excluyendo la propia película
        most_similar_products_indices = np.argsort(-product_similarities)[1:6]

        # Obtener los títulos de las 5 películas más similares
        most_similar_products_titles = data.loc[most_similar_products_indices, 'title'].tolist(
        )

        return {f'Las 5 películas más similares a {titulo} son': most_similar_products_titles}
    else:
        return "Película no encontrada"


@app.get('/recomendacion/{titulo}')
async def film_recommendation(titulo: str):
    """Obtiene una lista de las 5 películas más similares a la ingresada por el usuario.
    Args:
        titulo (str): ejemplo: 'Toy Story'
    Returns:
        _dict: ejemplo: Las cinco películas más similares a 'Toy Story' son: 
            ['The Hunt for Red October',
            'Babe',
            'Kill Bill: Vol. 2',
             'Kill Bill: Vol. 1',
            'Identity'].
    """

    try:
        # Busca la ruta del archivo en GitHub y crea el DataFrame como variable
        df = pd.read_csv('dataset/data_movies_ml.csv')
        # Aplicar la función para obtener el año, la cantidad de voto y el promedio de la película ingresada
        result = recomendacion(df, titulo)
        return JSONResponse(content=jsonable_encoder(result), media_type='application/json')
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail='Archivo .csv no encontrado, revisa si la ruta del archivo es correcta.')
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}.")
