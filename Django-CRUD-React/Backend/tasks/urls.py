from django.urls import path, include
from rest_framework.documentation import include_docs_urls #Modulo para documentar API
from rest_framework import routers
from tasks import views

#api versioning
router = routers.DefaultRouter()
router.register(r'tasks',views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('docs/', include_docs_urls(title="Tasks API")) #Ruta que documenta toda la API
]

#Todo este codigo ya esta generando las rutas GET, POST, PUT, DELETE