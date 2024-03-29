from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Fotografia
from .forms import FotografiaForms
from django.contrib import messages

def galeria(request):

    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')

        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    dados = {
        'fotografias': fotografias
    }

    return render(request, 'galeria/galeria.html', dados)

def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/image.html', {'fotografia':fotografia})

def buscar(request):

    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')

        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/galeria.html', {'fotografias':fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')
        return redirect('login')

    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia adicionada!')
            return redirect('home')

    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)

    if form.is_valid():
        form.save()
        messages.success(request, 'Fotografia editada com sucesso')
        return redirect('home')
    
    dados = {
        'form':form,
        'foto_id':foto_id
    }

    return render(request, 'galeria/editar_imagem.html', dados)

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada com suceso!')

    return redirect('home')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)

    dados = {
        'fotografias':fotografias,
    }

    return render(request, 'galeria/galeria.html', dados)
