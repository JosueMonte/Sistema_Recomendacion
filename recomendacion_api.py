from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Cargar el DataFrame
df = pd.read_csv('data_movies.csv')

# Mapeo de meses
month_mapping = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}


@app.get('/film_count_m')
def film_count_m(month: str):
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


if __name__ == "__recomendacion_api__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
