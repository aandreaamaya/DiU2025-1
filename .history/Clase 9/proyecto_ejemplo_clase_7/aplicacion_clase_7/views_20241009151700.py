from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
from .models import Producto  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Iniciar sesión automáticamente tras el registro
            return redirect('inicio')  # Redirigir a la página de inicio o productos
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

