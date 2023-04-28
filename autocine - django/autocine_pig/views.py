from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import RegistrarUsuarioForm, ContactoUsuarioForm
from django.contrib import messages

# Create your views here.

def index (request):
    
    context =  {

}

    return render (request, 'autocine_pig/index.html', context)

def complejos (request):

    context = {
    }

    return render (request, 'autocine_pig/complejos.html', context)

def valores (request):
    context = {

    }

    return render(request, 'autocine_pig/valores.html', context)

#aca ↓ defino la vista de registracion para el form

def registrar (request):

    if request.method == "POST":
        Registrar_Usuario_Form = RegistrarUsuarioForm(request.POST)

        if Registrar_Usuario_Form.is_valid():
            Registrar_Usuario_Form.cleaned_data['nombre']
            Registrar_Usuario_Form.cleaned_data['apellido']
            Registrar_Usuario_Form.cleaned_data['mail']
            Registrar_Usuario_Form.cleaned_data['fecha_De_Nacimiento']
            Registrar_Usuario_Form.cleaned_data['dni']
            Registrar_Usuario_Form.cleaned_data['password1']
            Registrar_Usuario_Form.cleaned_data['password2']


        messages.add_message(request, messages.SUCCESS, 'Te Registraste Correctamente')
        return redirect ('index')
    
    
    else:

        Registrar_Usuario_Form = RegistrarUsuarioForm()

    context = {'form' : Registrar_Usuario_Form}

    
    return render (request, 'autocine_pig/registrar.html', context)



def contacto (request):

    form = ContactoUsuarioForm() 
    
    context = {'form' : form
        
    }
    return render(request, 'autocine_pig/contacto.html', context)