from django.contrib import admin

# Register your models here.

from ventas.models import *

class ConcesionarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'nombre_gerente')
    search_fields = ('nombre', 'direccion')

admin.site.register(Concesionario, ConcesionarioAdmin)


class AutoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'anio_fabricacion', 'valor_minimo', 
        'valor_maximo', 'color', 'valor_alarma')
    raw_id_fields = ('concesionario',)

admin.site.register(Auto, AutoAdmin)


class MotoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'anio_fabricacion', 'valor_fijo_venta', 'tipo')
    raw_id_fields = ('concesionario',)
    
admin.site.register(Moto, MotoAdmin)

