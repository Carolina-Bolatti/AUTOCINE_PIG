from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('complejos/', views.complejos, name='complejos'),
    path('valores/', views.valores, name='valores'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('contacto/', views.contacto, name= 'contacto'),
    path('nosotros/', views.nosotros, name= 'nosotros'),
    path('login/', views.login, name= 'login')

]