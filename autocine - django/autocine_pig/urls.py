from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('complejos/', views.complejos, name='complejos'),
    path('valores/', views.valores, name='valores'),
    path('accounts/register/', views.register, name='register'),
    path('contacto/', views.contacto, name= 'contacto'),
    path('nosotros/', views.nosotros, name= 'nosotros'),
    path('reserva/', views.reserva, name= 'reserva'),


]