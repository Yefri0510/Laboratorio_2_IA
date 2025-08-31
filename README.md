# LABORATORIO 2

Yefri Stiven Barrero Solano - 2320392

# Primer punto

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

# Segundo punto

Con base a la tesis de maestría denominada: "Modelo de razonamiento basado en creencias, deseos en intenciones para la toma de decisiones en un algoritmo de planificación de trayectorias", se pueden establecer algunas definiciones como:

## **1. Agente inteligente** 
Es una entidad (que puede ser software o hardware) capaz de percibir su entorno a través de sensores, procesar esa información y actuar de manera racional sobre dicho entorno mediante actuadores, con el fin de maximizar un resultado esperado o cumplir sus objetivos de diseño. Su racionalidad se refleja en la capacidad de tomar decisiones correctas basadas en creencias y deseos, lo que le permite adaptarse, aprender y operar de forma autónoma en entornos dinámicos. Los agentes inteligentes son fundamentales en áreas como la robótica y la inteligencia artificial, donde se busca emular capacidades humanas de razonamiento y acción (Capítulos 3.1 y 4.1.3).

## **2. Campo de potencial artificial (APF)**
El método de Campos de Potenciales Artificiales (APF) es una técnica utilizada en robótica para la planificación de trayectorias. Se modela el espacio de trabajo como un campo de fuerzas virtuales donde:

* El **objetivo** genera un **campo de atracción** que atrae al robot como si fuera una partícula cargada positivamente.

* Los **obstáculos** generan **campos de repulsión** que alejan al robot para evitar colisiones.

La fuerza resultante que guía al robot es la suma vectorial de estas fuerzas. Aunque es un método sencillo y eficiente, tiene la limitación de que puede quedar atrapado en mínimos locales (puntos donde las fuerzas se anulan y el robot no puede avanzar hacia el objetivo), especialmente en entornos con obstáculos cóncavos o complejos (Capítulos 4.1.2.1 y 5).

## **3. Algoritmo BDI (Belief-Desire-Intention)**
El modelo BDI (Creencias, Deseos e Intenciones) es una arquitectura de razonamiento práctico inspirada en la psicología humana, utilizada para dotar de inteligencia y capacidad de decisión a agentes y robots. Sus componentes son:

* **Creencias (Beliefs):** Representan el conocimiento del robot sobre el estado actual del entorno (posición, obstáculos, objetivo), obtenido mediante percepción.

* **Deseos (Desires):** Son los objetivos o metas que el robot debe alcanzar (ej.: llegar a un destino, evitar obstáculos).

* **Intenciones (Intentions):** Son los planes o acciones concretas que el robot elige para cumplir sus deseos, basándose en sus creencias.

En el contexto de la tesis, el BDI se integra con el método APF para permitir que el robot **detecte y evade mínimos locales** mediante la reevaluación de sus creencias, la ajuste de sus deseos (ej.: buscar un objetivo intermedio) y cambie sus intenciones (ej.: modificar la ruta) de manera adaptativa (Capítulos 4.1.3.1 y 6).

# Tercer punto

Esta sección contiene dos enfoques para la navegación de un agente en un entorno con obstáculos: 
1. **CAMP_2.py**: Implementa un método basado únicamente en campos de potencial artificiales.
2. **Ejercicio_BDI.py**: Mejora el anterior combinando planificación global (A*) y control local (campos de potencial) con mecanismos de recuperación.
## CAMP_2.py: Navegación por Campos de Potencial
### Descripción
El archivo `CAMP_2.py` implementa un algoritmo de campos de potencial artificiales para guiar a un agente desde una posición inicial hasta un objetivo, evitando obstáculos. 
### Funcionamiento
- **Potencial Atractivo**: Atrae al agente hacia el objetivo con una fuerza proporcional a la distancia.
- **Potencial Repulsivo**: Aleja al agente de los obstáculos cuando se encuentra dentro de un radio de influencia.
- El movimiento del agente se calcula mediante el **gradiente negativo** del potencial total, moviéndose hacia regiones de menor energía.
### Limitaciones
- Puede quedar atrapado en **mínimos locales**.
- No garantiza encontrar una ruta en entornos complejos (ej: obstáculos en forma de herradura).
## Ejercicio_BDI.py: Planificación Híbrida (A* y Campos de Potencial)
### Descripción
El archivo `Ejercicio_BDI.py` extiende la lógica de `CAMP_2.py` con una arquitectura híbrida que combina planificación global y control local, superando las limitaciones del enfoque de campos de potencial puros.
### Componentes Principales
#### 1. Planificación Global con A*
- Genera una ruta inicial desde el inicio hasta el objetivo usando el algoritmo **A*** en un grid discretizado.
- Considera la inflación de obstáculos para evitar colisiones.
#### 2. Control Local con Campos de Potencial
- Utiliza una versión mejorada de campos de potencial para seguir los waypoints de la ruta global.
- Combina:
  - **Atracción** hacia el waypoint actual.
  - **Repulsión** de obstáculos cercanos.
#### 3. Detección de Estancamiento y Replanificación
- Monitorea el historial de posiciones para detectar si el agente está atrapado (ej: en mínimos locales).
- Si se detecta estancamiento, se **replanifica la ruta** usando A* desde la posición actual.
#### 4. Mecanismos de Recuperación
- Si falla la replanificación, aplica pequeñas **perturbaciones aleatorias** para escapar de mínimos locales.
- Limita el número de replanificaciones para evitar ciclos infinitos.
#### 5. Visualización Mejorada
- Muestra la ruta global (A*), waypoints, trayectoria real y el estado del agente en tiempo real.
- Incluye una gráfica de la **distancia al objetivo** para evaluar el progreso.
### Comparación de Enfoques
| Aspecto               | CAMP_2.py                          | Ejercicio_BDI.py                          |
|-----------------------|------------------------------------|-------------------------------------------|
| Planificación         | Local (gradiente)                 | Global (A*) + Local (campos de potencial) |
| Escape de mínimos     | No                                | Sí (replanificación + perturbaciones)     |
| Complejidad de obstáculos | Limitada                     | Alta (ej: herradura)                      |
| Robustez              | Baja                              | Alta                                      |
| Garantía de éxito     | No                                | Sí (si existe ruta)                       |
## Conclusión
**Ejercicio_BDI.py** implementa un **sistema híbrido BDI** (Belief-Desire-Intention) donde:
- **Creencias**: Representan el entorno (obstáculos, goal).
- **Deseos**: Llegar al objetivo.
- **Intenciones**: Seguir la ruta de A* y evitar obstáculos localmente.
Esta estrategia supera las limitaciones de los campos de potencial puros, siendo capaz de navegar en entornos complejos y escapar de situaciones de estancamiento mediante replanificación inteligente.


