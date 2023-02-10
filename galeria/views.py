from django.shortcuts import render
from django.http import HttpResponse

def galeria(request):
    return HttpResponse('<h1>Alura Space</h1>')