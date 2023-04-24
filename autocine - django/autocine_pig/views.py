from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import RegistrarUsuarioForm


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

    else:

        Registrar_Usuario_Form = RegistrarUsuarioForm()

    context = {'form' : Registrar_Usuario_Form}

    
    return render (request, 'autocine_pig/registrar.html', context)