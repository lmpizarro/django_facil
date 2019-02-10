

from django.urls import path, include

from .views import index, mascota_view, mascota_edit, mascota_list, mascota_delete

mascota_patterns = ([
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('listar/', mascota_list, name='mascota_listar'),
    path('editar/<int:id_mascota>', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>', mascota_delete, name='mascota_eliminar'),
], 'mascota')  # define a namespace


urlpatterns = [
    path('', include(mascota_patterns)),
]