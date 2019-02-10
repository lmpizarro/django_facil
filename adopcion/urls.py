from django.urls import path

from .views import index, solicitud_crear, solicitud_listar

app_name = 'adopcion'

urlpatterns = [
    path('', index, name='index'),
    path('crear', solicitud_crear, name='solicitud_crear'),
    path('crear', solicitud_listar, name='solicitud_listar'),

]