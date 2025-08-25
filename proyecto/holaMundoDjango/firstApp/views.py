from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>Hola Mundo, and... Diegx... ♨🎂</h1>")

def displayDatetime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora Actual: </b>" + str(dt)
    return HttpResponse(s)
