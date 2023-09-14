from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), #localhost:3000/
    path('about/', views.about),#localhost:3000/about/
    path('hello/<str:username>', views.hello), #Capturando paramas, str: espesifica que va ser un string 
    path('num/<int:id>',views.get_id), #Capturando el params, int: id
    path('projects/',views.project),
    path('tasks/<int:id>',views.tasks)

]
