from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Project, Task
from django.shortcuts import get_object_or_404, get_list_or_404 #Manejador de errores. 

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index page</h1>')
def hello(resquest,username):
    return HttpResponse(f'<h1>Hello {username}</h1>') #Obteniendo el params y mostrandolo.
def about(request):
    return HttpResponse('<h1>About</h1>')
def get_id(request,id):
    return HttpResponse(f'<h1>Obteniendo el id => {id}')

#
def project(request):
    projects = get_list_or_404(Project.objects.values()) #Haciendo peticion a la base de datos. Usar List para retornar multiples Objetos
    return JsonResponse(projects, safe=False)

def tasks(request,id):
    task = get_object_or_404(Task,id=id) #Usar object para retornar un objeto
    return HttpResponse(task.title)