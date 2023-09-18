## Instalaciones

Estas dos instalaciones se deben agregar a settings/INSTALLED_APPS y corsheaders.middleware.CorsMiddleware en setting/MIDDLEWARE antes de django.CommonMiddleware.
__API__:
~~~
pip install djangorestframework
~~~
__Paquete para evitar problemas con los Cors__:
~~~
pip install django-cors-headers
~~~

__Este codigo va al final de setting__ :
~~~
CORS_ALLOWD_ORIGINS = [  #Sirve para indicarle quien se puede conectar a nuestro servidor para hacer peticiones
    
]
~~~
## Modulo para Documentar API
~~~
pip install coreapi
~~~
Instalar en:
~~~
INSTALLED_APPS = [
    .... ,
    'coreapi',
    ....
]

# In settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
~~~