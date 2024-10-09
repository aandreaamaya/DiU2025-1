# admin.py

from django.contrib import admin
from .models import Fruta, Compra

# Registrar el modelo Fruta
@admin.register(Fruta)
class FrutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')  # Mostrar columnas en la lista de admin
    search_fields = ('nombre',)  # Añadir barra de búsqueda por nombre

# Registrar el modelo Compra
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fruta', 'cantidad', 'fecha')  # Mostrar columnas en la lista de admin
    list_filter = ('usuario', 'fecha')  # Añadir filtros por usuario y fecha
    search_fields = ('fruta__nombre',)  # Añadir barra de búsqueda por nombre de la fruta
