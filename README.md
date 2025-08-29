# LABORATORIO 2

## Primer punto

Python se ha consolidado como uno de los lenguajes más versátiles y poderosos para el manejo de datos y la visualización, gracias a su extenso ecosistema de librerías! Para el manejo de datos, cuenta con herramientas como Pandas, que permite manipular y analizar grandes volúmenes de información de manera eficiente, o NumPy, ideal para operaciones numéricas avanzadas. En el ámbito de las APIs de visualización, bibliotecas como Matplotlib ofrecen un control detallado sobre gráficos estáticos, mientras que Seaborn simplifica la creación de visualizaciones estadísticas atractivas. Para representaciones interactivas y dinámicas, Plotly y Bokeh permiten desarrollar dashboards y gráficos interactivos con solo unas líneas de código.

En cuanto a la representación intermedia, Altair se destaca por su enfoque declarativo, facilitando la construcción de visualizaciones a partir de transformaciones lógicas de los datos. Finalmente, para tareas de renderizado avanzado, Python integra librerías como Pygal (orientada a gráficos vectoriales escalables) o incluso opciones para renderizado 3D como Mayavi y Plotly 3D. Esta combinación de herramientas hace de Python una opción integral para científicos, ingenieros y diseñadores que buscan transformar datos en insights visuales de alto impacto. A continuación se habla acerca de algunas de ellas:

#1.Procesamiento y Manipulación de Datos

Estas librerías son el núcleo para la manipulación y el análisis de datos.

| Librería | Descripción | Caso de Uso Principal |
| :--- | :--- | :--- |
| **pandas** | Librería estándar para manipulación de datos en memoria (DataFrames). | Análisis de datos tabulares de tamaño pequeño a mediano. |
| **Dask** | Escala las operaciones de pandas y NumPy para datasets que no caben en memoria usando procesamiento paralelo. | Procesamiento distribuido de datos grandes en clusters. |
| **Polars** | Alternativa de alto rendimiento a pandas, escrita en Rust. Muy rápida para operaciones en columnas. | Manipulación rápida de datos en memoria, ideal para ETL. |
| **GeoPandas** | Extiende pandas para trabajar con datos geoespaciales. | Análisis y manipulación de datos en shapefiles, GeoJSON, etc. |
| **NetworkX** | Librería para la creación, manipulación y estudio de la estructura de grafos y redes. | Análisis de redes sociales, rutas, grafos de dependencias. |
| **xarray** | Maneja datos multidimensionales y etiquetados (ej. datos climáticos). | Datos científicos con dimensiones como tiempo, latitud, longitud. |
| **Ibis** | Proporciona una API de DataFrame que se traduce a SQL y se ejecuta en motores de bases de datos. | Análisis de datos directamente en bases de datos (BigQuery, Postgres). |
| **DuckDB** | Motor de base de datos analítica embebida. Se ejecuta in-process. | Consultas SQL rápidas sobre datos locales o en memoria. |
| **RAPIDS (cuDF)** | Ofrece una API similar a pandas para ejecutar operaciones de datos en GPUs NVIDIA. | Aceleración masiva de workflows de data science con GPU. |

## Segundo punto

## Tercer punto

