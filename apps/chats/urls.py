from django.urls import path

# Importación de Vistas
from apps.chats.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<room_name>', room, name='room'),
    #path('new', simulation, name='simulation_create'),
    #path('listar',  login_required(MascotaList.as_view()), name='mascota_listar'),
    #path('editar/<pk>', MascotaUpdate.as_view(), name='mascota_editar'),
    #path('eliminar/<pk>', MascotaDelete.as_view(), name='mascota_eliminar'),
]
