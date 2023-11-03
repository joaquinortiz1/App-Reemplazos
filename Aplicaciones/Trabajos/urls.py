from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes/', views.form),
    path('registrarTrabajo/', views.registrarTrabajo)
]