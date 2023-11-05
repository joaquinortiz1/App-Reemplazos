from django.db import models

# Create your models here.

#class Usuario(models.Model):
    #id=models.CharField(primary_key=True,max_length=6)
    #nombre = models.CharField(max_length=50)
    #email = models.EmailField(max_length=50)
    #password = models.CharField(max_length=128)

    #def __str__(self):
        #texto = "{0}"
        #return texto.format(self.nombre)


class Usuario(models.Model):
    # Campos de texto
    # nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre_usuario = models.CharField(max_length=50, unique=True, default='usuario_anonimo')
    nombre = models.CharField(max_length=50)
    # apellidos = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, null=False, default="Sin apellido")
    email = models.EmailField(unique=True)

    # Campos numéricos

    # Campos de fechas
    fecha_nacimiento = models.DateField(null=False, default="2000-01-01")
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')