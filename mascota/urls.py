

from django.urls import path, include

from .views import index, mascota_view, mascota_edit, mascota_list, mascota_delete
from .views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

mascota_patterns = ([
    path('', index, name='index'),
    path('nuevo/', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar/', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:pk>', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>', MascotaDelete.as_view(), name='mascota_eliminar'),
], 'mascota')  # define a namespace


urlpatterns = [
    path('', include(mascota_patterns)),
]