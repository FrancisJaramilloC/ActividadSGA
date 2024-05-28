from django.shortcuts import render

from mallaCurricular.models import Facultad, Carrera
from oferta.models import Prueba


def home(request):
    return render(request, 'index.html')

def facultades(request):
    facultades = Facultad.objects.all()
    context = {
        'facultades': facultades
    }
    return render(request, 'facultad.html', context)

def carreras(request):
    carrera = Carrera.objects.filter(facultad__nombre=prueba.nombre)
    prueba = Prueba.objects.all()
    context = {
        'carreras': carreras,
        'prueba': prueba

    }
    return render(request, 'carreras.html', context)

def carrera(request, id):
    carrera = Carrera.objects.get(id=id)
    context = {
        'carrera': carrera
    }
    return render(request, 'carreradetail.html', context)

