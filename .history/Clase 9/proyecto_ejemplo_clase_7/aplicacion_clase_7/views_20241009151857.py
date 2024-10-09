from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Fruta, Compra
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Vista para listar frutas disponibles
def lista_frutas(request):
    frutas = Fruta.objects.all()  # Obtener todas las frutas disponibles
    return render(request, 'lista_frutas.html', {'frutas': frutas})

# Vista para comprar una fruta
@login_required
def comprar_fruta(request, fruta_id):
    fruta = get_object_or_404(Fruta, id=fruta_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))

        # Verificar si hay suficiente stock
        if cantidad > fruta.stock:
            messages.error(request, 'No hay suficiente stock disponible.')
        else:
            # Registrar la compra
            Compra.objects.create(usuario=request.user, fruta=fruta, cantidad=cantidad)
            
            # Actualizar el stock de la fruta
            fruta.stock -= cantidad
            fruta.save()

            messages.success(request, f'Has comprado {cantidad} {fruta.nombre}(s).')

        return redirect('lista_frutas')

    return render(request, 'comprar_fruta.html', {'fruta': fruta})


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

