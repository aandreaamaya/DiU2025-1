from django.urls import path 
from . import views 
from .views import lista_productos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('productos/', lista_productos, name = 'lista_productos'),
    path('', views.inicio, name='inicio'), 
     # Página de registro
    path('registro/', views.registro_usuario, name='registro'),
    
    # Inicio de sesión (usando vistas genéricas de Django)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Cerrar sesión
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
    