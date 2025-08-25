from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayA(request):
    return HttpResponse("<h1>Hola Diegx desde la segnda pagina</h1>")