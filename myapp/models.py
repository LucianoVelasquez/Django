from django.db import models

# Create your models here. 
class Project(models.Model): #Declarando modelo
    name = models.CharField(max_length=200)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Relacionando esta tabla con la tabla Project