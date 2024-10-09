# models.py

from django.db import models
from django.contrib.auth.models import User  # Para asociar las compras al usuario

# Modelo de categorías 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
# Modelo de frutas
class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)  # Relación muchos a muchos con categorías

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} compró {self.cantidad} {self.fruta.nombre}(s)'
