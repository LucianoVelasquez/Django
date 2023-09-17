from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self): #Para mostarar el nombre de las tareas en el panel de admin.
        return self.title 