from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models import Producto  # Asegúrate de que Producto está correctamente importado

def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'lista_productos.html', {'productos': productos})
# Create your views here.

def saludo(resquest):
    return HttpResponse("Holaa (:")

class HolaMundoView(View):
    def get(self, reequest):
        return HttpResponse("Hola, esto es una vista bsada en clases :D")
    
def hola_mundo(request):
    contexto = {'mensaje': 'HOLA'}
    return render(request, 'hola_mundo.html', contexto)