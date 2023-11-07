from django.contrib import admin
from .models import Usuario, Curriculum, SolicitudDeReemplazo

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Curriculum)
admin.site.register(SolicitudDeReemplazo)