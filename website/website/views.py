from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def bienvenido(request):
    return HttpResponse("Bienvenido a TeLoVendo")

def inicio (request):
    saludo = "Bienvenido a TeLoVendo.cl"
    template = get_template('index.html')
    html = template.render({'bienvenida': saludo})
    return HttpResponse(html)