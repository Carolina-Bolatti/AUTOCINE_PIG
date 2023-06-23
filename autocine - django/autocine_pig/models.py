from django.db import models

class RegistrarUsuario (models.Model):
    nombre = models.CharField (max_length= 128, verbose_name= "Nombre")
    apellido = models.CharField (max_length= 128, verbose_name= "Apellido")
    mail = models.EmailField (max_length= 128, verbose_name= "Email")
    fecha_de_nacimiento = models.DateField (verbose_name= "Fecha_de_Nacimiento", default='1900-01-01')
    dni = models.IntegerField (verbose_name= "DNI: ",  null= True)
    password = models.CharField (max_length=128, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Login (models.Model):
    registrar_usuario = models.ForeignKey(RegistrarUsuario, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login de {self.registrar_usuario}"
    
class Pelicula(models.Model):
    titulo = models.CharField (max_length= 128, verbose_name= "Titulo")
    director = models.CharField (max_length= 128, verbose_name= "Director")
    actor_ppl = models.CharField (max_length= 128, verbose_name= "Actor Principal")

    def __str__(self):
        return f"{self.titulo} de {self.director} con {self.actor_ppl}"
    
class Complejo(models.Model):
    nombre = models.CharField (max_length= 128, verbose_name= "Complejo")
    direccion = models.CharField (max_length= 256, verbose_name= "Direccion")
    peliculas = models.ManyToManyField(Pelicula, related_name="Peliculas")

    def __str__(self):
        pelis = 'Peliculas:'
        for p in self.peliculas.all():
            pelis = pelis + ' [' + str(p) + ']'
        return f"{self.nombre} direccion: {self.direccion} {pelis}"
        
class Valore(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    valor = models.CharField(max_length=128, verbose_name="Valor")

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.valor}"
