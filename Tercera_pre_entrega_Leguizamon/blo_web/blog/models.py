from django.db import models
from django.contrib.auth.models import User

#class Usuario(models.Model):
 #   nombre = models.CharField(max_length=100)
  #  # Agregar cosas

class TemaDeDiscusion(models.Model):
    nombre = models.CharField(max_length=100)
    # Agregar cosas

#class NuevaDiscusion(models.Model):
 #   titulo = models.CharField(max_length=200)
  #  contenido = models.TextField()
   # tema = models.ForeignKey(TemaDeDiscusion, on_delete=models.CASCADE)
    # Agregar cosas
class NuevaDiscusion(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(TemaDeDiscusion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo