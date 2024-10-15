from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Fruta, Compra, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum
from django.utils.dateparse import parse_date
import json 
from .models import Notificacion, PreferenciasNotificacion
from datetime import datetime
import time
def estadisticas_frutas(request):
    # Obtener el usuario actual
    usuario = request.user

    # Filtros
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    categorias = request.GET.getlist('categorias')  # Obtener una lista de categorías seleccionadas

    # Filtrar las compras solo por el usuario actual
    compras = Compra.objects.filter(usuario=usuario)

    # Filtrar por rango de fechas si se especifica
    if fecha_inicio and fecha_fin:
        compras = compras.filter(fecha__range=[parse_date(fecha_inicio), parse_date(fecha_fin)])

    # Filtrar por múltiples categorías si se especifican
    if categorias:
        compras = compras.filter(fruta__categorias__id__in=categorias).distinct()

    # Obtener el total de frutas compradas por el usuario
    frutas_compradas = compras.values('fruta__nombre').annotate(total_compradas=Sum('cantidad')).order_by('-total_compradas')

    # Calcular el porcentaje de frutas compradas
    total_compras = compras.aggregate(total=Sum('cantidad'))['total'] or 0
    if total_compras > 0:
        for fruta in frutas_compradas:
            fruta['porcentaje'] = (fruta['total_compradas'] / total_compras) * 100
    else:
        for fruta in frutas_compradas:
            fruta['porcentaje'] = 0

    # Obtener todas las categorías para el formulario
    todas_categorias = Categoria.objects.all()

    # Preparar el contexto
    contexto = {
        'frutas_compradas': json.dumps(list(frutas_compradas)),
        'todas_categorias': todas_categorias,  # Enviar las categorías al formulario
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

@login_required
def configurar_notificaciones(request):
    usuario = request.user
    try:
        preferencias = PreferenciasNotificacion.objects.get(usuario=usuario)
    except PreferenciasNotificacion.DoesNotExist:
        preferencias = PreferenciasNotificacion(usuario=usuario)

    if request.method == 'POST':
        recibir_promociones = request.POST.get('recibir_promociones', False) == 'on'
        frecuencia = request.POST.get('frecuencia', 'semanal')

        # Guardar preferencias
        preferencias.recibir_promociones = recibir_promociones
        preferencias.frecuencia = frecuencia
        preferencias.save()

        return redirect('inicio')

    # Obtener notificaciones del usuario
    notificaciones = Notificacion.objects.filter(usuario=usuario).order_by('-fecha_creacion')

    contexto = {
        'preferencias': preferencias,
        'notificaciones': notificaciones  # Pasar las notificaciones al contexto
    }
    return render(request, 'configurar_notificaciones.html', contexto)

def enviar_notificaciones():
    # Filtrar los usuarios que deben recibir notificaciones según su preferencia de frecuencia
    hoy = datetime.now()

    usuarios_diarios = PreferenciasNotificacion.objects.filter(frecuencia='diaria')
    usuarios_semanales = PreferenciasNotificacion.objects.filter(frecuencia='semanal')
    usuarios_mensuales = PreferenciasNotificacion.objects.filter(frecuencia='mensual')

    for preferencias in usuarios_diarios:
        Notificacion.objects.create(usuario=preferencias.usuario, mensaje="¡Promoción diaria!")

    if hoy.weekday() == 0:  # Enviar notificaciones semanales solo los lunes
        for preferencias in usuarios_semanales:
            Notificacion.objects.create(usuario=preferencias.usuario, mensaje="¡Promoción semanal!")

    if hoy.day == 1:  # Enviar notificaciones mensuales solo el primer día del mes
        for preferencias in usuarios_mensuales:
            Notificacion.objects.create(usuario=preferencias.usuario, mensaje="¡Promoción mensual!")
            
