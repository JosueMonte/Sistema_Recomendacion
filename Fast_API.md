## Instalación:
pip install fastapi uvicorn

## Crear un archivo main.py - Código
from fastapi import FastAPI

app = FastAPI()

-- Define un endpoint usando el método HTTP GET --
@app.get('/') 
def read_root():
    return {"message": "Bienvenido a la API"}

@app.get('/endpoint1')
def endpoint1():
    return {"message": "Este es el endpoint 1"}

## Ejecutar en la terminal de powershell
uvicorn main:app --reload --port 8000
* main es el nombre del archivo (sin el .py).
* app es la instancia de FastAPI que creaste.
* --reload permite la recarga automática al modificar el código (útil en desarrollo).

## Acceder a la API
Entrar en el explorador y escribir: 
http://127.0.0.1:8000/

## Otras formas de acceder:
* Visita Swagger UI en: http://127.0.0.1:8000/docs
* Visita Redoc en: http://127.0.0.1:8000/redoc




