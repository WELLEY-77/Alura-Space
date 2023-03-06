from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia

def galeria(request):

    fotografias = Fotografia.objects.all()

    dados = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/galeria.html', dados)

def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/image.html', {'fotografia':fotografia})