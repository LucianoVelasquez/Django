from django.contrib import admin
from .models import Project, Task
# Register your models here.
admin.site.register(Project) #Guarda el modelo en la interfaz del admin
admin.site.register(Task)