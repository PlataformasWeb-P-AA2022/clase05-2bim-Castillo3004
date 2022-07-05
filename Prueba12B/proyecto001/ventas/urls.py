from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    # crear
    path('crear/concesionario', views.crear_concesionario, name='crear_concesionario'),
    path('crear/auto', views.crear_auto, name='crear_auto'),
    path('crear/moto', views.crear_moto, name='crear_moto'),
    path('crear/auto/concesionario/<int:id>', views.crear_auto_concesionario, name='crear_auto_concesionario'),
    path('crear/moto/concesionario/<int:id>', views.crear_moto_concesionario, name='crear_moto_concesionario'),
    
    # obtener 
    path('concesionario/<int:id>', views.obtener_concesionario, name='obtener_concesionario'),
    path('auto/<int:id>', views.obtener_auto, name='obtener_auto'),
    path('moto/<int:id>', views.obtener_moto, name='obtener_moto'),

    #editar
    path('editar_concesionario/<int:id>', views.editar_concesionario, name='editar_concesionario'),
    path('editar_auto/<int:id>', views.editar_auto, name='editar_auto'),
    path('editar_moto/<int:id>', views.editar_moto, name='editar_moto'),

    #eliminar
    path('eliminar/concesionario/<int:id>', views.eliminar_concesionario, name='eliminar_concesionario'),
    path('eliminar/auto/<int:id>', views.eliminar_auto, name='eliminar_auto'),
    path('eliminar/moto/<int:id>', views.eliminar_moto, name='eliminar_moto'),

]