from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('formulario_reg/', views.formulario),
    path('vista_admin/', views.vista_admin, name='vista_admin'),  
    path('vista_usuario/', views.vista_usuario, name='vista_usuario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'), 
    path('vista_usuario/curriculum_reg/', views.registrar_curriculum, name='registro_curriculum'), 
    #path('curriculum_edit/<int:curriculum_id>/', views.editar_curriculum, name='editar_curriculum'),
    #path('vista_curriculum/', views.vista_curriculum, name='vista_curriculum'),
    #path('registrar_curriculum/', views.registrar_curriculum, name='registrar_curriculum'),
    #path('confi_curriculum/', views.confirmacion_curriculum, name='confirmacion_curriculum'),
    #path('vista_usuario/curriculum_reg/confi_curri/', views.confir_curri, name='confirmacion_curri'),
    path('vista_admin/solicitudes/', views.form, name='solicitudes'),
    path('vista_admin/registrarTrabajo/', views.registrarTrabajo, name='registrar_trabajo'),
    path('vista_admin/solicitudes/edicionTrabajo/<id>', views.edicionTrabajo, name='editar_trabajo'),
    path('editarTrabajo/', views.editarTrabajo, name='edit_trabajo'),
    path('vista_admin/solicitudes/eliminacionTrabajo/<id>', views.eliminarTrabajo, name='eliminar_trabajo'),
    path('calcular_puntaje/', views.calcular_puntaje_curriculum, name='calcular_puntaje_curriculum'),
]