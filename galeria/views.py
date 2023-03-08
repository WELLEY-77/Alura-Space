from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia

def galeria(request):

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    dados = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/galeria.html', dados)

def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/image.html', {'fotografia':fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'fotografias':fotografias})