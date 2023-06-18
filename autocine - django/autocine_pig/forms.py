from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



TYPE_CHOICES = [
    ('', 'Seleccionar...'),
    ('Solicitud de información', 'Solicitud de información'),
    ('Reporte de problema', 'Reporte de problema'),
    ('Otro', 'Otro'),

]

class ContactoUsuarioForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=20, validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras y espacios')], required=True)
    consulta = forms.ChoiceField(choices=TYPE_CHOICES)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    comentario = forms.CharField(max_length=100, min_length=10, widget=forms.Textarea(attrs={ 'class' : 'area_texto'}))
    imagen = forms.ImageField(label='Cargar imagen', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        consulta = cleaned_data.get('consulta')
       
        if consulta == '':
            self.add_error('consulta', 'Debe seleccionar una opción')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label= "Email ", required= True)
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    dni = forms.CharField(label= "DNI ", max_length=8, validators=[RegexValidator(regex=r'^\d{8}$',
       message='El DNI ingresado no es válido', code='invalid_dni')], required= True)
    # password = forms.CharField(label="Contraseña", max_length=12, min_length=6, widget=forms.PasswordInput())
    # password2 = forms.CharField(label="Confirma Contraseña",max_length=12, min_length=6, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'dni','fecha_de_nacimiento', 'email']
        help_texts = {k:"" for k in fields }  