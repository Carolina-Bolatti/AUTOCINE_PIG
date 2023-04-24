from django import forms
from datetime import date



class RegistrarUsuarioForm(forms.Form):
    nombre = forms.CharField(label= "Nombre ", required= True)
    apellido = forms.CharField(label= "Apellido ", required= True)
    mail = forms.EmailField(label= "Email ", required= True)
    fecha_De_Nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-100, date.today().year+1)))
    dni = forms.CharField(label= "DNI ", required= True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    
    