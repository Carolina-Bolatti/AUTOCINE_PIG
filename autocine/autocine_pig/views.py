from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


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
