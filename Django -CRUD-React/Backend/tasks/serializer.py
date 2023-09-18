from rest_framework import serializers
from .models import Task
#Esta funcion sirve para "serializar" los datos a JSON. Convierte tipo de datos de python a JSON.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description', 'done') #Aca indicamos que capos queremos serializar.
        fields = '__all__'  #Serializamos todo