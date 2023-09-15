from django.db import models

# Create your models here. 
class Project(models.Model): #Declarando modelo
    name = models.CharField(max_length=200)
    
    def __str__(self): #Methodo que sirve para mostrar el nombre en la interfaz del Admin
        return self.name 
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Relacionando esta tabla con la tabla Project
    
    def __str__(self): #Methodo que sirve para mostrar el nombre en la interfaz del Admin
        return (f'{self.title} - {self.project}')