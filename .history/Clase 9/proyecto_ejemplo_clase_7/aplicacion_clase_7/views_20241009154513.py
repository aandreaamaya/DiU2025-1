from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Fruta, Compra
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum
from django.utils.dateparse import parse_date
import json 
# Vista para mostrar las estadísticas de las frutas más compradas
def estadisticas_frutas(request):
    # Filtros
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    categoria = request.GET.get('categoria')

    compras = Compra.objects.all()

    # Filtrar por rango de fechas si se especifica
    if fecha_inicio and fecha_fin:
        compras = compras.filter(fecha__range=[parse_date(fecha_inicio), parse_date(fecha_fin)])

    # Filtrar por categoría si se especifica
    if categoria:
        compras = compras.filter(fruta__categoria=categoria)

    # Obtener el total de frutas compradas
    frutas_compradas = compras.values('fruta__nombre').annotate(total_compradas=Sum('cantidad')).order_by('-total_compradas')

    # Calcular el porcentaje de frutas compradas
    total_compras = compras.aggregate(total=Sum('cantidad'))['total'] or 0
    if total_compras > 0:
        for fruta in frutas_compradas:
            fruta['porcentaje'] = (fruta['total_compradas'] / total_compras) * 100
    else:
        for fruta in frutas_compradas:
            fruta['porcentaje'] = 0

    # Enviar los datos a la plantilla
    contexto = {
        'frutas_compradas': json.dumps(list(frutas_compradas)),
    }
    return render(request, 'estadisticas_frutas.html', contexto)

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

