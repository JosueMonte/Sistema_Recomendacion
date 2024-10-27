## 1. Comprensión de los Datos
* __Carga y revisión inicial__: Importa el dataset y revisa las primeras filas para entender la estructura, formato y tipos de datos.
* __Resumen estadístico__: Utiliza funciones como describe() para ver estadísticas básicas (media, mediana, desviación estándar, valores mínimo y máximo, percentiles) para variables numéricas.
* __Información general__: Usa info() para verificar el tipo de datos (int, float, object), valores nulos, y la memoria que ocupa cada columna.
* __Dimensiones del dataset__: Revisa el número de filas y columnas.

## 2. Limpieza de Datos
* __Valores anidados__: Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.
* __Chequeo de nulos__: Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.
* __Chequeo de nulos__: Los valores nulos del campo release date deben eliminarse.
* __Formateo__: De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.
* __Eliminar columnas__: Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.
* __Crear columnas__: Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.
* __Opcionales__: 
* __Valores atípicos (outliers)__: Detecta valores anómalos que pueden afectar los modelos. Usa gráficos como boxplots o medidas estadísticas.
* __Valores duplicados__: Revisa y elimina filas duplicadas si es necesario.

## 3. Análisis Univariado
* __Visualización de distribución de variables__: Usa gráficos como histogramas, diagramas de densidad o diagramas de caja para entender la distribución de cada variable individualmente.
* __Análisis estadístico de los datos__: Revisa la media, mediana, moda, varianza y desviación estándar de cada variable para identificar sesgos o patrones.

## 4. Análisis Bivariado y Multivariado
* __Correlación__: Calcula la matriz de correlación para identificar relaciones lineales entre variables numéricas. Utiliza gráficos como heatmaps para visualizarlos.
* __Gráficos de dispersión (scatter plots)__: Para ver la relación entre dos variables numéricas.
* __Boxplots__: Para analizar la relación entre una variable categórica y una numérica.
* __Tablas de contingencia__: Para analizar la relación entre variables categóricas.
* __Gráficos de pares (pair plots)__: Para entender relaciones multivariadas en un solo gráfico.

## 5. Ingeniería de Características
* __Creación de nuevas variables__: Genera nuevas características que puedan aportar más valor al modelo.
* __Codificación de variables categóricas__: Convierte las variables categóricas en numéricas usando técnicas como One-Hot Encoding, Label Encoding, etc.
* __Normalización/Estandarización__: Escala los datos numéricos para que estén en un rango uniforme (útil para algoritmos que son sensibles a la escala).
* __Reducción de dimensionalidad__: Usa técnicas como PCA o t-SNE si hay demasiadas características y quieres simplificar el modelo.

## 6. Visualización Avanzada
* __Distribución de la variable objetivo__: Analiza la variable que quieres predecir, especialmente si es desbalanceada.
* __Análisis multivariado avanzado__: Usa gráficos como gráficos de burbuja, gráficos de violin o gráficos de radar para visualizar relaciones más complejas.
* __Visualización de relaciones temporales__: Si hay un componente temporal, analiza patrones estacionales o tendencias.

## 7. Preparación para el Modelado
* __División del dataset__: Separa los datos en conjuntos de entrenamiento y prueba/validación (por ejemplo, 70% - 30% o 80% - 20%).
* __Selección de características__: Elige las características que utilizarás en el modelo en función del análisis realizado.
* __Transformaciones finales__: Aplica las transformaciones necesarias (escalado, codificación) en los datos.