from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_menu(request):
    return HttpResponse('¡Hola! Bienvenido a ACE ¿Qué deseas hacer?<br>1.Agregrar plantilla<br>2.Ingresar al banco de preguntas<br>3.Generar evaluación<br>')

