## Armar el cronograma de trabajar con Notion para llegar a la fecha
## Resolver el EDA hasta el punto 2.
* Crear un entorno virtual
    * escribir en la terminal: python -m venv venv
    * crear archivos: .gitignore y requirements.txt
    * enviar venv a .gitingore
    * instalar las librerias necesarias 
    * utilizar pip freeze > requirements.txt (para actualizar el .txt, si es necesario instalar mas librerias, hay que ejecutar el codigo de nuevo)
*  EDA:
    * outliers o anomalias.
    * nubes de palabras para ver las más frecuentes.
    * gráficas:
        * nubes de palabras con las palabras más frecuentes en los título de las películas.
    * encontrar similitud con otras películas, podría ser por puntaje.
## Desarrollo de la API
* Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:
    * Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
    
* Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil:
    * https://docs.render.com/free#free-web-services
    * https://github.com/HX-FNegrete/render-fastapi-tutorial

* render deployado sistema_de_recomendacion_de_peliculas (api montada en la nube con render):
    * https://sistema-de-recomendacion-de-peliculas-8cnl.onrender.com/

* fastapi (es local, vinculo mi puerto con la api al servidor web):
    * http://127.0.0.1:8000/
    * http://127.0.0.1:8000/docs
## Video
* Menor a 7 minutos.
* Mostrar las consultas requeridas en funcionamiento desde la API.
* Breve explicación del modelo utilizado para el sistema de recomendación.
* Explicar EDA, ETL y desarrollo de la API.

## Criterios de evaluación
* codigo: comentar con strings.
* repositorio: orden de archivos y carpetas, readme.md presentando proyecto y trabajo realizado. Yo dentro de 1.5 años deberia entenderlo.
* entregar link de YouTube de acceso al video. Usarlo en modo incognito para comprobar que es publico. 

# Recomnedación:
    * Hacer un dataset chico para la funcion 1 y probar en render. Funcion de mes
    * Hacer otro para la funcion 2 y deployar en render. Funcion de dia.
    * Hacer otro para la función de recomendación de películas con ML y deployar en render. Esto tendria que terminarlo el viernes.
    * Método de explode en pandas para desanidar.
    * Crear un data set para desanidar las columnas.
    * Recortar los datos en todo sentido, no hay problemas: eliminar peliculas viejas, quedarnos con la de habla hispana, baja puntuación, pocas votaciones... eliminar links, posters.
    * Subir los archivos en parquet.
    * Requirement puede tirar error, en cuyo caso habria que hacerlo manual
    * Crear un dataset con 2 mil filas, con pocas columnas, llamo con la funcion a ver si tira bien y me fijo si corre en render.
    



