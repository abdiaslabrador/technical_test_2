# Prueba técnica
Esto es una prueba técnica para practicar habilidades en django rest framework.
Se debe desarrollar una API para consultar la unidad de fomento (SII) por medio de un endpoint, el cuál tendrá como función hacer scrapping a la página de sii para obtener el valor de la tabla de registros de Unidad de Fomento que se actualiza cada año

# Metas
El Servicio de Impuestos Internos (SII) de Chile mantiene una tabla con los valores de la Unidad de Fomento actualizados para cada año. Tu desafío consiste en crear una API en Python que permita a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica utilizando scraping.

-	La API debe estar desarrollada en Python utilizando la librería "requests" u otra similar.
-	Para la API puedes usar el Framework que mas te guste.
-	No se puede utilizar Selenium debido al alto consumo de recursos que estas herramientas implican.
-	La API debe permitir consultar el valor de la Unidad de Fomento para una fecha específica, la cual debe ser ingresada como parámetro en la solicitud.
-	La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.
-	La API debe devolver el valor de la Unidad de Fomento correspondiente a la fecha consultada.
-	La respuesta de la API debe estar en formato JSON.


Para ayudarte en el desarrollo de este desafío, puedes utilizar la tabla de valores de la Unidad de Fomento actualizados para cada año que se encuentra en el siguiente enlace: https://www.sii.cl/valores_y_fechas/uf/uf2023.htm

# Endpoint
-	GET: Obtiene el valor de unidad de fomento (SII) al pasarle la fecha como parámetro ejemplo: http://127.0.0.1:8000/sii/?fecha=1-08-2022

![Sin título2](https://github.com/abdiaslabrador/technical_test_2/assets/44957286/6210cb30-d94f-4a83-93e4-5f7df79001b2)


# Tecnología utilizada
- Python 3.12 (última hasta el momento)
- Django 5.0
- Django REST Framework 3.14.0
- beautifulsoup4 4.12.2

# Instalación (sin usar docker)
1- Para correr la aplicación se debe contar con Python en la version 3.12 (Python: https://www.python.org/downloads/).

2- Se recomienda usar un entorno virtual para trabajar:

  Para crear el entorno virtual: ```python -m venv env```

  Para activar el entorno virtual: ```env\Scripts\activate.bat```

3- Al activar el entorno virtual ejecuta el siguiente comando para instalar las dependencias del proyecto:

```pip install -r requirements.txt```


4- Dentro del entorno virtual ejecutar las migraciones con el comando:

```python manage.py migrate```

5- Finalmente, ejecutar el proyecto con:

```python manage.py runserver```

# Instalación y configuración usando docker

- Vete a la raíz del proyecto y ejecuta este comando para instalar la imagen y cada dependencia necesaria en el proyecto:

```docker compose build```

Cuando finalice la instalación ejecuta el siguiente comando para correr el servidor:

```docker compose up```

Ya corriendo el servidor dirígete a http://localhost:8000/ y verás la aplicación corriendo
