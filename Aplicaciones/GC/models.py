from django.db import models
from django.utils import timezone


#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.


class Usuario(models.Model):
    # Campos de texto
    nombre_usuario = models.CharField(max_length=50, unique=True, default='usuario_anonimo')
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, null=False, default="Sin apellido")
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128, default='valor_predeterminado')
    rut = models.CharField(max_length=12, unique=True, default='N/A')
    habilidades_usuario = models.CharField(max_length=50, choices=[("programacion", "programacion"), ("liderazgo", "liderazgo")], default="programacion")
    experiencia_usuario = models.CharField(max_length=50, choices=[("asistente_ejecutivo", "asistente_ejecutivo"), ("coordinador_proyecto", "coordinador_proyecto"), ("gerente_de_seguridad", "gerente_de_seguridad"), ("desarrollador_backend", "desarrollador_backend"), ("desarrollador_frontend", "desarrollador_frontend"), ("desarrollador_full_stack", "desarrollador_full_stack"), ("especialista_en_recursos_humanos", "especialista_en_recursos_humanos"), ("especialista_en_ventas", "especialista_en_ventas"), ("especialista_en_soporte Técnico", "especialista_en_soporte Técnico"), ("especialista_en_logística", "especialista_en_logística"), ("analista_financiero", "analista_financiero")], default="asistente_ejecutivo")
    fecha_nacimiento = models.DateField(null=False, default="2000-01-01")
    ultimo_login = models.DateTimeField(auto_now=True)
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

    # Relación Usuario - Curriculum
    cve = models.OneToOneField('Cv', on_delete=models.CASCADE, null=True, blank=True)


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

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
#Modelos en desarrollo
class Educacion(models.Model):
    nombre = models.CharField(max_length=100)

class Idioma(models.Model):
    nombre = models.CharField(max_length=100)

class Experiencia(models.Model):
    nombre = models.CharField(max_length=100)
#Modelos en desarrollo

class SolicitudDeReemplazo(models.Model):
    #id = models.CharField(max_length=10, primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos = models.TextField()
    ubicacion = models.CharField(max_length=50, choices=[("iquique", "iquique"), ("alto_hospicio", "alto_hospicio")])
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_trabajo = models.CharField(max_length=50, choices=[("Tiempo completo", "Tiempo completo"), ("Medio tiempo", "Medio tiempo"), ("Freelance", "Freelance"), ("Reemplazo", "Reemplazo")])
    tipo_de_contrato = models.CharField(max_length=50, choices=[("Indefinido", "Indefinido"), ("Temporal", "Temporal")])
    area_de_trabajo = models.CharField(max_length=50, choices=[("Tecnología", "Tecnología"), ("Salud", "Salud"), ("Finanzas", "Finanzas"), ("Educación", "Educación"), ("Marketing", "Marketing"), ("Ventas", "Ventas"), ("Recursos Humanos", "Recursos Humanos"), ("Ingeniería", "Ingeniería"), ("Arte y Diseño", "Arte y Diseño"), ("Legal", "Legal"), ("Medio Ambiente", "Medio Ambiente"), ("Investigación", "Investigación"), ("Servicios Sociales", "Servicios Sociales"), ("Otros", "Otros")])
    fecha_de_publicacion = models.DateField(auto_now_add=True)
    trabajo_remoto = models.BooleanField()
    fecha_limite = models.DateField()
    habilidades_requeridas = models.CharField(max_length=50, choices=[("programacion", "programacion"), ("liderazgo", "liderazgo")], default="programacion")
    experiencia_requerida = models.CharField(max_length=50, choices=[("asistente_ejecutivo", "asistente_ejecutivo"), ("coordinador_proyecto", "coordinador_proyecto"), ("gerente_de_seguridad", "gerente_de_seguridad"), ("desarrollador_backend", "desarrollador_backend"), ("desarrollador_frontend", "desarrollador_frontend"), ("desarrollador_full_stack", "desarrollador_full_stack"), ("especialista_en_recursos_humanos", "especialista_en_recursos_humanos"), ("especialista_en_ventas", "especialista_en_ventas"), ("especialista_en_soporte Técnico", "especialista_en_soporte Técnico"), ("especialista_en_logística", "especialista_en_logística"), ("analista_financiero", "analista_financiero")], default="asistente_ejecutivo")
    educacion_requerida = models.CharField(max_length=50, choices=[("basica", "basica"), ("Media", "Media"), ("Superior", "Superior")], default="basica")
    abierto = models.BooleanField(default=True)

    def __str__(self):
        texto  = "{0} {1}"
        return texto.format(self.titulo, self.requisitos)
    
    # Relación SolicitudDeReemplazo - Curriculum
    cve = models.ManyToManyField('Cv', related_name='solicitudes')


class Cv(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    area_trabajo = models.CharField(max_length=50, choices=[("Tecnología", "Tecnología"), ("Salud", "Salud"), ("Finanzas", "Finanzas"), ("Educación", "Educación"), ("Marketing", "Marketing"), ("Ventas", "Ventas"), ("Recursos Humanos", "Recursos Humanos"), ("Ingeniería", "Ingeniería"), ("Arte y Diseño", "Arte y Diseño"), ("Legal", "Legal"), ("Medio Ambiente", "Medio Ambiente"), ("Investigación", "Investigación"), ("Servicios Sociales", "Servicios Sociales"), ("Otros", "Otros")])
    telefono = models.CharField(max_length=20)
    experiencia_laboral = models.CharField(max_length=30, choices=[("Asistente ejecutivo", "Asistente ejecutivo"), ("Coordinador de proyecto", "Coordinador de proyecto"), ("Gerente seguridad", "Gerente seguridad"), ("Desarrollador backend", "Desarrollador backend"), ("Desarrollador frontend", "Desarrollador frontend"), ("Desarrollador full stack", "Desarrollador full stack")])
    anios_experiencia = models.PositiveIntegerField()
    educacion = models.CharField(max_length=30, choices=[("basica", "basica"), ("Media", "Media"), ("Superior", "Superior")])
    habilidades = models.CharField(max_length=30, choices=[("Programacion", "Programacion"), ("Primeros auxilios", "Primeros auxilios"), ("Liderazgo", "Liderazgo"), ("Creatividad e innovación", "Creatividad e innovación"), ("Trabajo en equipo", "Trabajo en equipo")])
    idiomas = models.CharField(max_length=30, choices=[("Español", "Español"), ("Ingles", "Ingles"), ("Español e ingles", "Español e ingles"), ("Español, ingles y frances", "Español, ingles y frances"), ("Español, ingles y portugues", "Español, ingles y portugues")])


class Postulacion(models.Model):
    curriculum = models.ForeignKey(Cv, on_delete=models.CASCADE, default=1)
    solicitud = models.ForeignKey(SolicitudDeReemplazo, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.curriculum.nombre} - {self.solicitud.titulo}"
