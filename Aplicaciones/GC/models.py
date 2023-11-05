from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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

    # Campos importantes
    contrasena = models.CharField(max_length=128, default='valor_predeterminado')
    rut = models.CharField(max_length=12, unique=True)

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

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, email, contrasena=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(nombre_usuario=nombre_usuario, email=email, **extra_fields)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, email, contrasena, **extra_fields):
        extra_fields.setdefault('es_personal', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(nombre_usuario, email, contrasena, **extra_fields)
    
