# Sistema de gestion de recursos educativos digitales

[ ![Codeship Status for agilesg4/PryFinalAgiles20182](https://app.codeship.com/projects/26013ab0-bfaa-0136-6260-628ad8a7bead/status?branch=master)](https://app.codeship.com/projects/313377)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/02f1cef710074cc8958ab94c6c9378f9)](https://www.codacy.com/app/drummerwilliam/PryFinalAgiles20182?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=agilesg4/PryFinalAgiles20182&amp;utm_campaign=Badge_Grade)

Este es un proyecto de desarrollo por sprints realizado en Django para el curso de procesos de metodologías ágiles MISO4101 en la universidad de los Andes. Se trata de un sistema de gestion de recursos digitales utilizados por la unidad CONECTA-TE de la universidad para realizar apoyo tecnologico y multimedia a las clases de la universidad.

## Getting Started

Sigue estas instrucciones para tener una copia del proyecto corriendo localmente en tu maquina. Ver la seccion de despliegue para mas información.

### Prerequisitos

Para este proyecto se usaron las siguientes tecnologias.
*  Python ver. 2.7.10
*  Django ver. 1.11.15
*  PostgreSQL

Al clonar el proyecto no olvidar correr el siguiente comando para instalar todas las depedencias.
```
pip install -r requirements.txt
```

### Instalación y despliegue

Con python y el entorno virtual correctamente configurado nos dirigimos a la carpeta donde esta ubicado el archivo manage.py y ejecutamos los siguientes comandos.

Hacemos las migraciones de los modelos

```
python manage.py makemigrations polls
```
Corremos las migraciones

```
python manage.py migrate 
```
De este modo tendremos la base de datos necesaria para correr el proyecto. Finalmente ejecutamos el siguiente comando para ejecutar el servidor, el cual estara disponible para nosotros en http://127.0.0.1:8000/
```
python manage.py runserver 
```

### Variables de entorno para Heroku

ON_CODESHIP=False</br>
ON_HEROKU=True</br>
DISABLE_COLLECTSTATIC=1</br>

Tambien es necesario una base de datos de tipo Postgresql

## Built With

* [Django](https://www.djangoproject.com/) - El framework de python que utilizamos
