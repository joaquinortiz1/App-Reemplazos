from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('formulario_reg/', views.formulario),
    path('vista_admin/', views.vista_admin, name='vista_admin'),  
    path('vista_usuario/', views.vista_usuario, name='vista_usuario'),  
]