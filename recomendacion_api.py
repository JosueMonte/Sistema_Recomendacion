from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
import pandas as pd

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
