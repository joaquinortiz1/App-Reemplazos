from django.db import models

# Create your models here.
#class Especialidad(models.Model):
    # Definición de campos de la especialidad
    #nombre = models.CharField(max_length=255)
    # Otros campos

    #def __str__(self):
        #return self.nombre


class SolicitudDeTrabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos = models.TextField()
    ubicacion = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_trabajo = models.CharField(max_length=20, choices=[("Tiempo completo", "Tiempo completo"), ("Medio tiempo", "Medio tiempo"), ("Por horas", "Por horas")])
    tipo_de_contrato = models.CharField(max_length=20, choices=[("Indefinido", "Indefinido"), ("Temporal", "Temporal"), ("Freelance", "Freelance")])
    area_de_trabajo = models.CharField(max_length=50)
    fecha_de_publicacion = models.DateField(auto_now_add=True)
    #especialidades_buscadas = models.ManyToManyField("Especialidad")
    trabajo_remoto = models.BooleanField()
    fecha_limite = models.DateField()

    def __str__(self):
        texto  = "{0} {1}"
        return texto.format(self.titulo, self.requisitos)