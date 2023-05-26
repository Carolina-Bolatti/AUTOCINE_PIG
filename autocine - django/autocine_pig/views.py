from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import RegistrarUsuarioForm, ContactoUsuarioForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import RegistrarUsuario, Login, Pelicula, Complejo, Valor
from django.views.generic import ListView



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

    peliculas = Pelicula.objects.all()
    context = {
        'peliculas': peliculas
    }

    return render(request, 'autocine_pig/complejos.html', context)



def valores(request, pelicula_id=None):
    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula_id')
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        complejos = Complejo.objects.filter(peliculas=pelicula)
        valores = Valor.objects.filter(peliculas=pelicula)
        

        context = {
            'pelicula': pelicula,
            'complejos': complejos,
            'valores': valores,
            'pelicula_id': pelicula_id
        }

        return render(request, 'autocine_pig/valores.html', context)

    peliculas = Pelicula.objects.all()
    context = {
        'peliculas': peliculas,
        
    }

    return render(request, 'autocine_pig/valores.html', context)








def registrar_usuario (request):
    if request.method == "POST":
        Form = RegistrarUsuarioForm(request.POST)
        
        if Form.is_valid():
            nombre = Form.cleaned_data['nombre']
            apellido = Form.cleaned_data['apellido']
            mail = Form.cleaned_data['mail']
            fecha_de_nacimiento = Form.cleaned_data['fecha_de_nacimiento']
            dni = Form.cleaned_data['dni']
            password = Form.cleaned_data['password']


            nuevo_usuario = RegistrarUsuario(
            nombre=nombre,
            apellido=apellido,
            mail=mail,
            fecha_de_nacimiento=fecha_de_nacimiento,
            dni=dni,
            password=password
        )

            
            nuevo_usuario.save()
    
            nuevo_login = Login(registrar_usuario=nuevo_usuario)
            nuevo_login.save()

        
        messages.add_message(request, messages.SUCCESS, 'Te Registraste Correctamente')
        return redirect('index')
    else:
        Form = RegistrarUsuarioForm()
    return render(request, 'autocine_pig/registrar_usuario.html', {'form':  Form})




            
    
    

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


#dejo todo preparado para configurar el user a la base de datos
def login (request):
    form = LoginForm (request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'autocine_pig/login.html', {'form': form})
