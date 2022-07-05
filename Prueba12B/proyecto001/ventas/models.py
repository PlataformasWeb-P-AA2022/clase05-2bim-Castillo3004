from pyexpat import model
from django.db import models

# Create your models here.

class Concesionario(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    nombre_gerente = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.direccion,
                self.nombre_gerente)
    
    def obtener_costo_autos(self):
        valor = [t.valor_maximo for t in self.losvehiculos.all()]
        valor = sum(valor)
        return valor

    def obtener_costo_motos(self):
        valor = [c.valor_fijo_venta for c in self.lasmotos.all()]
        valor = sum(valor)
        return valor



class Auto(models.Model):
    marca = models.CharField(max_length=30)
    anio_fabricacion = models.IntegerField()
    valor_minimo = models.DecimalField(max_digits=100, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=100, decimal_places=2)
    color = models.CharField(max_length=30)
    valor_alarma = models.DecimalField(max_digits=100, decimal_places=2)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name="losvehiculos")

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.marca,
            self.anio_fabricacion,
            self.valor_minimo,
            self.valor_maximo,
            self.color,
            self.valor_alarma)


class Moto(models.Model):
    marca = models.CharField(max_length=30)
    anio_fabricacion = models.IntegerField()
    valor_fijo_venta = models.DecimalField(max_digits=100, decimal_places=2)

    tipo_opciones = (('Trabajo', 'Trabajo'),
                ('Deportiva','Deportiva'))

    tipo = models.CharField(max_length=30 ,choices=tipo_opciones)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name="lasmotos")

    def __str__(self):
        return "%s %s %s %s" %(self.marca,
            self.anio_fabricacion,
            self.valor_fijo_venta,
            self.tipo)
