from django.urls import path, include
from rest_framework import routers
from tasks import views

#api versioning
router = routers.DefaultRouter()
router.register(r'tasks',views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1/',include(router.urls)),
]

#Todo este codigo ya esta generando las rutas GET, POST, PUT, DELETE