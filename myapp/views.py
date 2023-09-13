from django.http import HttpResponse 
from django.http import HttpRequest

# Create your views here.
def hello(resquest):
    return HttpResponse('<h1>Hello Wordl</h1>')
def about(request):
    return HttpResponse('<h1>About</h1>')