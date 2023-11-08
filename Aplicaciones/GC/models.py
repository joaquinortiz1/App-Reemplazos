from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    rut = models.CharField(max_length=12, unique=True, default='N/A')

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


class Curriculum(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    area_trabajo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    experiencia_laboral = models.TextField()
    anios_experiencia = models.PositiveIntegerField()
    educacion = models.TextField()
    habilidades = models.TextField()
    idiomas = models.TextField()
    curriculum_adjunto = models.FileField(upload_to='curriculums/')

    #def __str__(self):
        #return self.nombre

class SolicitudDeReemplazo(models.Model):
    #id = models.CharField(max_length=10, primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos = models.TextField()
    ubicacion = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_trabajo = models.CharField(max_length=20, choices=[("Tiempo completo", "Tiempo completo"), ("Medio tiempo", "Medio tiempo"), ("Por horas", "Por horas")])
    tipo_de_contrato = models.CharField(max_length=20, choices=[("Indefinido", "Indefinido"), ("Temporal", "Temporal"), ("Freelance", "Freelance"), ("Reemplazo", "Reemplazo")])
    area_de_trabajo = models.CharField(max_length=50)
    fecha_de_publicacion = models.DateField(auto_now_add=True)
    trabajo_remoto = models.BooleanField()
    fecha_limite = models.DateField()

    def __str__(self):
        texto  = "{0} {1}"
        return texto.format(self.titulo, self.requisitos)


class Cv(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    area_trabajo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    experiencia_laboral = models.CharField(max_length=30, choices=[("Asistente ejecutivo", "Asistente ejecutivo"), ("Coordinador de proyecto", "Coordinador de proyecto"), ("Gerente seguridad", "Gerente seguridad"), ("Desarrollador backend", "Desarrollador backend"), ("Desarrollador frontend", "Desarrollador frontend"), ("Desarrollador full stack", "Desarrollador full stack")])
    anios_experiencia = models.PositiveIntegerField()
    educacion = models.CharField(max_length=30, choices=[("basica", "basica"), ("Media", "Media"), ("Superior", "Superior")])
    habilidades = models.CharField(max_length=30, choices=[("Programacion", "Programacion"), ("Primeros auxilios", "Primeros auxilios"), ("Liderazgo", "Liderazgo"), ("Creatividad e innovación", "Creatividad e innovación"), ("Trabajo en equipo", "Trabajo en equipo")])
    idiomas = models.CharField(max_length=30, choices=[("Español", "Español"), ("Ingles", "Ingles"), ("Español e ingles", "Español e ingles"), ("Español, ingles y frances", "Español, ingles y frances"), ("Español, ingles y portugues", "Español, ingles y portugues")])