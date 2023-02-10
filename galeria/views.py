from django.shortcuts import render
from django.http import HttpResponse

def galeria(request):
    return render(request, 'galeria/galeria.html')