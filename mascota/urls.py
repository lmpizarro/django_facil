

from django.urls import path, include

from .views import index, mascota_view, mascota_edit, mascota_list, mascota_delete
from .views import MascotaList, MascotaCreate

mascota_patterns = ([
    path('', index, name='index'),
    path('nuevo/', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar/', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:id_mascota>', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>', mascota_delete, name='mascota_eliminar'),
], 'mascota')  # define a namespace


urlpatterns = [
    path('', include(mascota_patterns)),
]