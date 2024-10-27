from fastapi import FastAPI

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
