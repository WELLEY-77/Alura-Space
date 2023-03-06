from django.shortcuts import render
from django.http import HttpResponse
from .models import Fotografia

def galeria(request):

    fotografias = Fotografia.objects.all()

    dados = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/galeria.html', dados)

def image(request):
    return render(request, 'galeria/image.html')