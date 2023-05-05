from django.db import models

class RegistrarUsuario (models.Model):
    nombre = models.CharField (max_length= 128)
    apellido = models.CharField (max_length= 128)
    mail = models.EmailField (max_length= 128)
    
