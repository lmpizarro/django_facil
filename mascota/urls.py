

from django.urls import path, include

from .views import index, mascota_view, mascota_crear, mascota_listar

mascota_patterns = ([
    path('', index, name='index'),
    path('view/', mascota_view, name='mascota_view'),
    path('listar/', mascota_crear, name='mascota_crear'),
    path('crear/', mascota_listar, name='mascota_listar')
], 'mascota')  # define a namespace


urlpatterns = [
    path('', include(mascota_patterns)),
]