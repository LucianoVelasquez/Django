# Django - Python

## 1 - Iniciando entorno virtual
~~~
pip install virtualenv
~~~
Para crear el entorno virtual:
~~~
virtualenv venv
~~~
Para entrar al entorno virtual (Utilizar CMD):
~~~
.\venv\Scripts\activate
~~~
## 2 - Instalando Django
En el entorno virtual
~~~
pip install django
~~~
### Iniciando projecto:
~~~
django-admin startproject "nombre" .
~~~
### Para ejecutar el proyecto:
~~~
python manage.py runserver 3000
~~~ 
### Para administrar el proyecto:
~~~
python manage.py help
~~~ 
### Estructura del proyecto:
* ____Init__.py__: sirve para decirle que la carpeta que lo contiene es un modulo. 
* __pycache__: cache de python
* __settings.py__: sirve para configurar todo el proyecto
  * __ALLOWEB_HOSTS__: permite al servidor web que direcciones tiene permitido consultar a nuestro servidor
  * __DEBUG__: Indica a la aplicacion si estamos en modo de desarrollo o en produccion.
### _Los proyectos en django se dividen en distintas aplicaciones_.
Por ejemplo distintas secciones:
* __blog__
* __store__
* __tasks__
### Para crear estos apartados usamos:
~~~
python manage.py startapp 'nombreApp'
~~~
### Estructura de la App:
* __Views (archivo principal)__: se puede definir lo que se puede enviar al cliente ejemplo HTML.
* __migrations__: carpeta que esta relacionada con la BD
* __app__:  archivo que maneja las configuraciones de la app
* __models__: donde vamos a definir los modelos de la BD mediante clases
* __tests__: para hacer test de las views y otros.