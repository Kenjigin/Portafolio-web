from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('galeria/<slug:slug>/', views.galeria, name='galeria_categoria'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('contacto/', views.contacto, name='contacto'),
]
