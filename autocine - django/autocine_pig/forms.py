from django import forms
from datetime import date
from django.core.validators import RegexValidator



TYPE_CHOICES = [
    ("Reserva" , "Reserva"),
    ("Complejos" , "Complejos"),
    ("Otros" , "Otros"),

]

class RegistrarUsuarioForm(forms.Form):
    nombre = forms.CharField(label= "Nombre ", required= True)
    apellido = forms.CharField(label= "Apellido ", required= True)
    mail = forms.EmailField(label= "Email ", required= True)
    fecha_De_Nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-100, date.today().year+1)))
    dni = forms.CharField(label= "DNI ", required= True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    


class ContactoUsuarioForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=20, validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras y espacios')], required=True)
    consulta = forms.ChoiceField(choices=TYPE_CHOICES)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    comentario = forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'area_texto'}))
    imagen = forms.ImageField(label='Cargar imagen', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    
    
    