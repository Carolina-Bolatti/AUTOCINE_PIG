from django.db import models

class RegistrarUsuario (models.Model):
    nombre = models.CharField (max_length= 128, verbose_name= "Nombre")
    apellido = models.CharField (max_length= 128, verbose_name= "Apellido")
    mail = models.EmailField (max_length= 128, verbose_name= "Email")
    fecha_De_Nacimiento = models.DateField (verbose_name= "Fecha de Nacimiento", default='1900-01-01')
    dni = models.IntegerField (verbose_name= "DNI: ",  null= True)
    password = models.CharField (max_length=128, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Login (models.Model):
    registrar_usuario = models.ForeignKey(RegistrarUsuario, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login de {self.registrar_usuario}"
    
