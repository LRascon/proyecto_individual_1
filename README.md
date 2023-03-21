
# Proyecto MVP de Transformación de Datos y Desarrollo de API

Este proyecto consiste en la transformación de datos, desarrollo de una API con consultas específicas, análisis exploratorio de datos y creación de un sistema de recomendación de películas para usuarios.

## Transformación de Datos

Para este MVP, se han aplicado las siguientes transformaciones a los datos:

- Generación de campo id: Cada id se compone de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
- Reemplazo de los valores nulos del campo rating por el string “G” (corresponde al maturity rating: “general for all audiences”)
- Formato AAAA-mm-dd para las fechas
- Todos los campos de texto en minúsculas
- Conversión del campo duration en dos campos: duration_int y duration_type. El primero es un integer y el segundo es un string que indica la unidad de medición de duración: min (minutos) o season (temporadas)

## Desarrollo de API

Se ha propuesto disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que se han desarrollado son las siguientes:

- Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))
- Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
- Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
- Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))

## Deployment

Se ha utilizado Render para el deployment de la API. También se ha considerado Railway, aunque se requiere dockerización.
Se puede acceder a la API en la siguiente dirección: https://proyecto-individual-1-vyop.onrender.com/docs

## Análisis exploratorio de datos

Se ha realizado un análisis exploratorio de datos utilizando librerías como pandas profiling, sweetviz, autoviz, entre otros. Se han identificado relaciones entre las variables de los datasets, se han detectado outliers y anomalías y se han encontrado patrones interesantes que pueden ser explorados en un análisis posterior. 
En el siguiente enlace podran observar el EDA desplegado con la ayuda de profiling: https://lrascon.github.io/proyecto_individual_1/edaDataStreaming.html

## Sistema de recomendación

Una vez que se han limpiado los datos y se ha realizado un análisis exploratorio, se ha desarrollado un sistema de recomendación de películas para usuarios. Este sistema es capaz de recomendar o no una película para un usuario específico, dado un id de usuario y una película. Se ha desplegado el sistema de recomendación en una interfaz gráfica utilizando Gradio.

##### ¡Gracias por leer! Siéntete libre de contactarme si tienes alguna pregunta o comentario.

## Autor

- Nombre: Luis F. Rascón
- Email: luis.francisco.rc@gmail.com
- GitHub: LRascon
###End

