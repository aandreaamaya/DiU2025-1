from django.urls import path 
from . import views 
from .views import HolaMundoView
from .views import lista_productos

urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),
    path('hola-clase/', HolaMundoView.as_view(), name='hola_clase'),
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('productos/', lista_productos, name = 'lista_productos')
]
    