# Sistema de gestion de recursos educativos digitales

Este es un proyecto de desarrollo por sprints realizado en Django para el curso de procesos de metodologías ágiles MISO4101 en la universidad de los Andes. Se trata de un sistema de gestion de recursos digitales utilizados por la unidad CONECTA-TE de la universidad para realizar apoyo tecnologico y multimedia a las clases de la universidad.

## Getting Started

Sigue estas instrucciones para tener una copia del proyecto corriendo localmente en tu maquina. Ver la seccion de despliegue para mas información.

### Prerequisitos

Para este proyecto se usaron las siguientes tecnologias.
* Python ver. 2.7.10
* Django ver. 1.11.15
* PostgreSQL

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
Creamos el script de la base de datos

```
python manage.py sqlmigrate polls 
```
Realizamos las migraciones

```
python manage.py migrate 
```
De este modo tendremos la base de datos necesaria para correr el proyecto. Finalmente ejecutamos el siguiente comando para ejecutar el servidor, el cual estara disponible para nosotros en http://127.0.0.1:8000/
```
python manage.py runserver 
```

## Built With

* [Django](https://www.djangoproject.com/) - El framework de python que utilizamos
