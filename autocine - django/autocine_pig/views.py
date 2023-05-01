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

            
            messages.add_message(request, messages.SUCCESS, 'Te Registraste Correctamente')
            return redirect('index')
    else:
        Registrar_Usuario_Form = RegistrarUsuarioForm()
    return render(request, 'autocine_pig/registrar.html', {'form':  Registrar_Usuario_Form})
            
    
    
    

    




def contacto (request):

    if request.method == 'POST':
        form = ContactoUsuarioForm(request.POST, request.FILES)
        if form.is_valid():

        
            messages.add_message(request, messages.SUCCESS, '¡Tu mensaje ha sido enviado con éxito!')
        
            return redirect('index')
    
    else:
        messages.error(request, 'Por favor, corrige los errores del formulario.')
        form = ContactoUsuarioForm()
    return render(request, 'autocine_pig/contacto.html', {'form': form})