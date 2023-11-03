from django.urls import path
from . import views

urlpatterns = [
    path ('solicitudes/', views.form)
]