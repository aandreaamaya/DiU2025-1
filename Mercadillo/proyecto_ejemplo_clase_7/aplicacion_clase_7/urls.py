from django.urls import path 
from . import views 

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.inicio, name='inicio'), 
     # Página de registro
    path('registro/', views.registro_usuario, name='registro'),
    
    # Inicio de sesión (usando vistas genéricas de Django)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Cerrar sesión
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('frutas/', views.lista_frutas, name='lista_frutas'),
    path('comprar/<int:fruta_id>/', views.comprar_fruta, name='comprar_fruta'),
    path('estadisticas/', views.estadisticas_frutas, name='estadisticas_frutas'),

    path('configurar_notificaciones/', views.configurar_notificaciones, name='configurar_notificaciones'),
]
    