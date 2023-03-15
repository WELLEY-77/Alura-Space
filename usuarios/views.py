from django.shortcuts import render,redirect
from .forms import LoginForms, CadastoForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):

    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password = senha,
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success( request, f'{nome} logado com sucesso')
                return redirect('home')
            else:
                messages.error(request,'Erro ao efetuar login')
                return redirect('login')


    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):

    form = CadastoForms()

    if request.method == 'POST':
        form = CadastoForms(request.POST)

    if form.is_valid():
        if form['senha_1'].value() != form['senha_2'].value():
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        
        nome = form['nome_cadastro'].value()
        email = form['email'].value()
        senha= form['senha_1'].value()
        
        if User.objects.filter(username=nome).exists():
            messages.error('Usuario ja cadastrado')
            return redirect('cadastro')
        
        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
        )
        usuario.save()
        messages.success('Login efetuado com sucesso')
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('login')
