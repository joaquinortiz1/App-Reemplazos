from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('formulario_reg/', views.formulario),
    path('vista_admin/', views.vista_admin, name='vista_admin'),  
    path('vista_usuario/', views.vista_usuario, name='vista_usuario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'), 
    path('vista_usuario/curriculum_reg/', views.registrar_curriculum, name='registrar_curriculum'), 
    path('curriculum_edit/<int:curriculum_id>/', views.editar_curriculum, name='editar_curriculum'),
    path('vista_curriculum/', views.vista_curriculum, name='vista_curriculum'),
    path('solicitudes/', views.form, name='solicitudes'),
    path('registrarTrabajo/', views.registrarTrabajo, name='registrar_trabajo'),
]