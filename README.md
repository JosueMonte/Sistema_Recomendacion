# Sistema de recomendación de películas

Este repositorio contiene varios endpoints que brindan información sobre películas y además, cuenta con uno en especial que es capaz de recomendar una película en base a una que le haya gustado.

## Descripción
Se desarrollan dos fases para el proyecto:

- `Ingeniería de datos.`
- `Modelamiento y evaluación con machine learning.`

#### Ingeniería de datos

En esta fase se realizan diversas transformaciones en los datos provenientes del dataset de películas, como ser:

- `Eliminación de columnas irrelevantes`.
- `Eliminación de filas irrelevantes.`
- `Desanidado de columnas`.
- `Formateo de columnas`.

Y se realiza un análisis exploratorio o EDA, abordando problemas como:

- `Valores faltantes o nulos.`
- `Datos duplicados y variables irrelevantes`.
- `Valores outliers o anómalos`.
- `Análisis univariado.`

#### Modelamiento y evaluación con machine learning

Se implementa un modelo de clasificación con aprendizaje supervisado, que calcula con un algoritmo de coseno de similitud, las cinco películas más similares. Las variables consideradas son:

- `release_year (año de lanzamiento)`
- `budget (presupuesto utilizado)`
- `popularity (popularidad)`
- `vote_average (puntaje promedio)`
- `genres_name (géneros)`
- `studios_name (compañías)`

Además, se desarrollan otros endpoints que son capaces de:

-  `Devolver la cantidad de películas lanzadas según día de la semana ingresado`.
-  `Devolver la cantidad de películas lanzadas según mes ingresado`.
-  `Devolver año de estreno y puntuación según película ingresada`.
-  `Devolver año de estreno, cantidad de votaciones y puntuación promedio`.

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/JosueMonte/Sistema_Recomendacion
   ```

2. Instala los paquetes requeridos en el archivo:
   ```sh
   requirements.txt
   ```

## Notebooks disponibles

- `transformaciones_1.ipynb`: Se realizan las transformaciones para que corran los primeros 4 endpoints. 
- `transformaciones_2.ipynb`: Se realizan las transformaciones para el consiguiente análisis exploratorio.
- `eda.ipynb`: Se realizan un análisis exploratorio de los datos,  para que corra el modelo de machine learning.
- `machine_learning.ipynb`: Se prueba el algoritmo de similitud de coseno considerando distintas variables de entrada.

## API

- `recomendacion_api.py`: Contiene las funciones con los 5 endpoints. 

## Ejecución de la API en render

Interactúa con la API siguiendo el siguiente link:
   ```sh
https://sistema-de-recomendacion-de-peliculas-8cnl.onrender.com/docs
   ```
