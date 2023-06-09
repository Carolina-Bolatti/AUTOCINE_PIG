from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ContactoUsuarioForm, UserRegisterForm

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Pelicula, Complejo, Valore




# Create your views here.


def index (request, pelicula_id=None):
    peliculas = Pelicula.objects.all()
    context = {
        'peliculas' : peliculas,
        'pelicula_id': pelicula_id,
    }

    return render (request, 'autocine_pig/index.html', context)

def complejos (request, pelicula_id=None):
    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula_id')
        pelicula = Pelicula.objects.get(id=pelicula_id)
        complejos = Complejo.objects.filter(peliculas=pelicula)


        context = {
            'pelicula': pelicula,
            'complejos': complejos,
            'pelicula_id': pelicula_id,
            
        }

        return render(request, 'autocine_pig/complejos.html', context)
    if request.method == 'GET':
#    peliculas = Pelicula.objects.all()
     complejos = Complejo.objects.all()
    context = {
#        'peliculas': peliculas
        'complejos': complejos
    }

    return render(request, 'autocine_pig/complejos.html', context)

def valores(request, pelicula_id=None):
    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula_id')
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        complejos = Complejo.objects.filter(peliculas=pelicula)
        valores = Valore.objects.filter(pelicula=pelicula)
        context = {
            'pelicula': pelicula,
            'complejos': complejos,
            'valores': valores,
            'pelicula_id': pelicula_id
        }
        return render(request, 'autocine_pig/valores.html', context)

    pelicula_id = request.GET.get('pelicula_id')
    if pelicula_id:
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        valores = Valore.objects.filter(pelicula=pelicula)
    else:
        pelicula = None
        valores = None

    peliculas = Pelicula.objects.all()
    context = {
        'peliculas': peliculas,
        'pelicula': pelicula,
        'pelicula_id': pelicula_id,
        'valores': valores
    }
    return render(request, 'autocine_pig/valores.html', context)

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

def nosotros (request):
    context = {

    }

    return render(request, 'autocine_pig/nosotros.html', context)

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            # messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request,'registration/register.html', context)

@login_required
def reserva (request):
    return render (request, 'autocine_pig/reserva.html')
