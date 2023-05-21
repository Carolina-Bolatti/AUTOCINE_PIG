from django import forms
from datetime import date
from django.core.validators import RegexValidator






TYPE_CHOICES = [
    ('', 'Seleccionar...'),
    ('Solicitud de información', 'Solicitud de información'),
    ('Reporte de problema', 'Reporte de problema'),
    ('Otro', 'Otro'),

]

class RegistrarUsuarioForm(forms.Form):
    nombre = forms.CharField(label= "Nombre ", required= True)
    apellido = forms.CharField(label= "Apellido ", required= True)
    mail = forms.EmailField(label= "Email ", required= True)
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    dni = forms.CharField(label= "DNI ", max_length=8, validators=[RegexValidator(regex=r'^\d{8}$',
        message='El DNI ingresado no es válido', code='invalid_dni')], required= True)
    password1 = forms.CharField(label="Contraseña", max_length=12, min_length=6, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repita Contraseña",max_length=12, min_length=6, widget=forms.PasswordInput())
    

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
            
        
        return self
    


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


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        
    
    