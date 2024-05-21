from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import clienteForm

# Create your views here.

def index(request):
    return HttpResponse(request,'<h1>Olá mundo.<h1>')

def pagina(request):
    return render(request,'index.html')

def agendar_secao(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = clienteForm()
    return render(request,'agendar_secao.html',{'form': form})

def listar_clientes(request):
    lista = Cliente.objects.all()
    return render(request,'listar_clientes.html', {'lista': lista})

def senai(request):
    return render(request,'senai.html')