from django.contrib import admin
from .models import Usuario, Curriculum, SolicitudDeReemplazo, Cv

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Curriculum)
admin.site.register(Cv)
admin.site.register(SolicitudDeReemplazo)