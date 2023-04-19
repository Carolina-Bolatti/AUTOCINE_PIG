from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('complejos/', views.complejos, name='complejos'),
    path('valores/', views.valores, name='valores')

]