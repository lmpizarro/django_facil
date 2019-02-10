from django.urls import path

from .views import index, SolicitudCreate, solicitud_listar, SolicitudList

app_name = 'adopcion'

urlpatterns = [
    path('', index, name='index'),
    path('solicitud/listar/', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva/', SolicitudCreate.as_view(), name='solicitud_crear'),

]