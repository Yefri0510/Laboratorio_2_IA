# LABORATORIO 2

Yefri Stiven Barrero Solano - 2320392

## Primer punto

Python se ha consolidado como uno de los lenguajes más versátiles y poderosos para el manejo de datos y la visualización, gracias a su extenso ecosistema de librerías! Para el manejo de datos, cuenta con herramientas como Pandas, que permite manipular y analizar grandes volúmenes de información de manera eficiente, o NumPy, ideal para operaciones numéricas avanzadas. En el ámbito de las APIs de visualización, bibliotecas como Matplotlib ofrecen un control detallado sobre gráficos estáticos, mientras que Seaborn simplifica la creación de visualizaciones estadísticas atractivas. Para representaciones interactivas y dinámicas, Plotly y Bokeh permiten desarrollar dashboards y gráficos interactivos con solo unas líneas de código.

En cuanto a la representación intermedia, Altair se destaca por su enfoque declarativo, facilitando la construcción de visualizaciones a partir de transformaciones lógicas de los datos. Finalmente, para tareas de renderizado avanzado, Python integra librerías como Pygal (orientada a gráficos vectoriales escalables) o incluso opciones para renderizado 3D como Mayavi y Plotly 3D. Esta combinación de herramientas hace de Python una opción integral para científicos, ingenieros y diseñadores que buscan transformar datos en insights visuales de alto impacto. A continuación se habla acerca de algunas de ellas:

## 1. Procesamiento y Manipulación de Datos

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

## 2. Visualización y Graficación

Este conjunto de librerías se utiliza para crear visualizaciones estáticas e interactivas.

#### APIs de Alto Nivel
*   **.plot() de pandas**: API rápida y conveniente basada en matplotlib para crear gráficos estáticos directamente desde un DataFrame.
*   **hvPlot**: API unificada y minimalista que genera gráficos interactivos (usando Bokeh o Plotly como backend) desde pandas, Dask o xarray con muy poco código.

### Representación Intermedia (Abstracción)
*   **HoloViews**: Se enfoca en la semántica de los datos más que en los detalles visuales. Define la visualización y luego la renderiza con Bokeh o matplotlib. Ideal para construir visualizaciones complejas de manera declarativa.
*   **Datashader**: Diseñada para visualizar conjuntos de datos extremadamente grandes (miles de millones de puntos). Primero rasteriza los datos para luego aplicar colores, permitiendo visualizar big data sin colapsar el navegador.

### Motores de Renderizado (Backends)
*   **matplotlib**: La librería fundamental para visualizaciones estáticas en Python. Altamente personalizable pero con una API más verbosa.
*   **Bokeh**: Especializada en crear visualizaciones interactivas para navegadores web. Ideal para dashboards y aplicaciones de data apps.
*   **Plotly**: Similar a Bokeh, con un fuerte enfoque en la interactividad inmediata y la capacidad de crear dashboards en la nube fácilmente.

## 3. Aplicaciones Web y Dashboards

*   **Streamlit**: Framework para convertir scripts de datos en aplicaciones web interactivas de manera extremadamente rápida. Se integra perfectamente con la mayoría de las librerías de visualización (Matplotlib, Plotly, Bokeh, etc.).

## Segundo punto

Con base a la tesis de maestría denominada: "Modelo de razonamiento basado en creencias, deseos en intenciones para la toma de decisiones en un algoritmo de planificación de trayectorias", se pueden establecer algunas definiciones como:

### **1. Agente inteligente** 
Es una entidad (que puede ser software o hardware) capaz de percibir su entorno a través de sensores, procesar esa información y actuar de manera racional sobre dicho entorno mediante actuadores, con el fin de maximizar un resultado esperado o cumplir sus objetivos de diseño. Su racionalidad se refleja en la capacidad de tomar decisiones correctas basadas en creencias y deseos, lo que le permite adaptarse, aprender y operar de forma autónoma en entornos dinámicos. Los agentes inteligentes son fundamentales en áreas como la robótica y la inteligencia artificial, donde se busca emular capacidades humanas de razonamiento y acción (Capítulos 3.1 y 4.1.3).

### **2. Campo de potencial artificial (APF)**
El método de Campos de Potenciales Artificiales (APF) es una técnica utilizada en robótica para la planificación de trayectorias. Se modela el espacio de trabajo como un campo de fuerzas virtuales donde:

* El objetivo genera un campo de atracción que atrae al robot como si fuera una partícula cargada positivamente.

* Los obstáculos generan campos de repulsión que alejan al robot para evitar colisiones.

La fuerza resultante que guía al robot es la suma vectorial de estas fuerzas. Aunque es un método sencillo y eficiente, tiene la limitación de que puede quedar atrapado en mínimos locales (puntos donde las fuerzas se anulan y el robot no puede avanzar hacia el objetivo), especialmente en entornos con obstáculos cóncavos o complejos (Capítulos 4.1.2.1 y 5).

### **3. Algoritmo BDI (Belief-Desire-Intention):**
El modelo BDI (Creencias, Deseos e Intenciones) es una arquitectura de razonamiento práctico inspirada en la psicología humana, utilizada para dotar de inteligencia y capacidad de decisión a agentes y robots. Sus componentes son:

* **Creencias (Beliefs):** Representan el conocimiento del robot sobre el estado actual del entorno (posición, obstáculos, objetivo), obtenido mediante percepción.

* **Deseos (Desires):** Son los objetivos o metas que el robot debe alcanzar (ej.: llegar a un destino, evitar obstáculos).

* **Intenciones (Intentions):** Son los planes o acciones concretas que el robot elige para cumplir sus deseos, basándose en sus creencias.

En el contexto de la tesis, el BDI se integra con el método APF para permitir que el robot detecte y evade mínimos locales mediante la reevaluación de sus creencias, la ajuste de sus deseos (ej.: buscar un objetivo intermedio) y cambie sus intenciones (ej.: modificar la ruta) de manera adaptativa (Capítulos 4.1.3.1 y 6).

## Tercer punto

