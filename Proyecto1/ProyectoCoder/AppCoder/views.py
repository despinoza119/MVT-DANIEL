from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from AppCoder.models import Tio,Primo

# Create your views here.
def tio(self):
    miHtml=open("C:/Users/Daniel/Desktop/MVT+DANIEL/Proyecto1/ProyectoCoder/plantillas/template1.html")

    plantilla=Template(miHtml.read())

    data=Tio.objects.all()

    tios={
        "tios":data
    }

    miContexto=Context(tios)

    documento =plantilla.render(miContexto)

    return HttpResponse(documento)

def primo(self):
    miHtml=open("C:/Users/Daniel/Desktop/MVT+DANIEL/Proyecto1/ProyectoCoder/plantillas/template2.html")

    plantilla=Template(miHtml.read())

    data=Primo.objects.all()

    primos={
        "primos":data
    }

    miContexto=Context(primos)

    documento =plantilla.render(miContexto)

    return HttpResponse(documento)