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
    fecha_De_Nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    dni = forms.CharField(label= "DNI ", max_length=8, validators=[RegexValidator(regex=r'^\d{8}$',
        message='El DNI ingresado no es válido', code='invalid_dni')], required= True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repita Contraseña",widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        if password2 and len(password2) < 6:
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres')

        return password2
    


class ContactoUsuarioForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=20, validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras y espacios')], required=True)
    consulta = forms.ChoiceField(choices=TYPE_CHOICES)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    comentario = forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'area_texto'}))
    imagen = forms.ImageField(label='Cargar imagen', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        consulta = cleaned_data.get('consulta')
        comentario = cleaned_data.get('comentario')

        if consulta == '':
            self.add_error('consulta', 'Debe seleccionar una opción')

        if comentario and len(comentario) < 10:
            self.add_error('comentario', 'El comentario debe tener al menos 10 caracteres') 
    
    