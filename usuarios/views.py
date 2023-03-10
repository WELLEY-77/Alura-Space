from django.shortcuts import render
from .forms import LoginForms, CadastoForms

def login(request):

    form = LoginForms()

    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):

    form = CadastoForms()

    return render(request, 'usuarios/cadastro.html', {'form':form})
