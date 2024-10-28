## Preparar el data set para las primeras 6 funciones, para ello:
*** Me olvido del sistema de recomendación. Voy a crear un data set muy sencillo que corra en render. ***
* 1. Eliminar filas:
    * del original_language y quedarme con EN (aclarar en el README que el análisis será en habla inglesa)
* 2. Eliminar columnas: 
    * belongs_to_collection
    * genres
    * poster_path
    * homepage
    * imdb_id
    * overview
    * production_companies
    * production_countries
    * original_language (primero eliminar filas que no sean en idioma EN)
    * runtime
    * spoken_languages
    * tagline
    * title (me quedo con la columna original_title) (bueno hay que pensarlo bien, puede ser a la inversa)
    * video (primero eliminar las filas vacías)
* 3. Separar columnas: 
    * del release_date en: dia, mes, anio
* 4. Eliminar filas:
    * del release_date: antiguas a 1990, es decir, solo me quedo desde 1990 en adelante (aclarar en el README)
    * del status: las que no fueron released, es decir, solo me quedo con releases (aclarar en el README)
    * del video: eliminar las filas vacías.
* 5. Correr la api en render de esta forma, sino continuar eliminando filas, podría ser:
    * vote_average < 5
    * vote_count < 100


