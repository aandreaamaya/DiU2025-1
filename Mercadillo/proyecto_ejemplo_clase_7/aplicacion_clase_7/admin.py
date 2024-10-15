# admin.py

from django.contrib import admin
from .models import Fruta, Compra, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Fruta)
class FrutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    filter_horizontal = ('categorias',)  # Mostrar las categorías en un selector
