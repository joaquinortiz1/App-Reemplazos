from django.db import models

# Create your models here.

class Usuario(models.Model):
    id=models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
