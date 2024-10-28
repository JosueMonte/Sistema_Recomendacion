from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
import pandas as pd
import os

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


def film_count_m(df, month: str):
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
    filtered_df = df[df['month'] == month_number]
    # Contar los IDs en las filas filtradas
    count_ids = filtered_df['id'].count()
    return {"endpoint0": f"Fueron estrenadas {count_ids} peliculas en el mes de {month}"}


@app.get('/film_count_m/{month}')
async def film_cant_mes(month: str):
    """Obtiene la cantidad de filmaciones según mes desde un archivo en formato csv
    Args:
        month (str): ejemplo: "enero"
    Returns:
        _type_: ejemplo: 2000 filmaciones en el mes de enero
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists("dataset/data_movies.csv"):
            raise FileNotFoundError(
                "Archivo csv no encontrado, revisa si la ruta del archivo es correcta.")

        # Leer el archivo CSV
        df = pd.read_csv("dataset/data_movies.csv")

        # Imprimir las primeras filas del DataFrame para verificar
        print(df.head())

        # Aplicar la función para obtener la cantidad de filmaciones según mes aplicado
        result = film_count_m(df, month)
        return JSONResponse(content=jsonable_encoder(result), media_type="application/json")
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail="Archivo csv no encontrado, revisa si la ruta del archivo es correcta.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al leer el archivo csv: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
