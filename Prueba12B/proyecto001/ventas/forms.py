from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from ventas.models import *

class ConcesionarioForm(ModelForm):
    class Meta:
        model = Concesionario
        fields = ['nombre', 'direccion', 'nombre_gerente']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'nombre_gerente': _('Ingrese el nombre completo del gerente por favor'),
        }
        
    def clean_nombre_gerente(self):
        valor = self.cleaned_data['nombre_gerente']
        num_palabras = len(valor.split())

        if num_palabras < 4:
            raise forms.ValidationError("Ingrese dos nombres y dos apellidos por favor")
        return valor


class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'anio_fabricacion', 'valor_minimo', 'valor_maximo', 'color', 'valor_alarma', 'concesionario']
        labels = {
            'anio_fabricacion': _('Año Fabricacion'),
        }

    def clean_anio_fabricacion(self):
        valor = self.cleaned_data['anio_fabricacion']

        if valor > 2022:
            raise forms.ValidationError("El año de fabricacion no puede ser mayor al año actual")
        return valor

    def clean_valor_maximo(self):
        valor = self.cleaned_data['valor_maximo']
        if (valor) > 100000:
            raise forms.ValidationError("El valor maximo no puede ser mayor a 10000")
        return valor
    


class MotoForm(ModelForm):
    class Meta:
        model = Moto
        fields = ['marca', 'anio_fabricacion', 'valor_fijo_venta', 'tipo', 'concesionario']
        labels = {
            'anio_fabricacion': _('Año Fabricacion'),
        }   

    def clean_anio_fabricacion(self):
        valor = self.cleaned_data['anio_fabricacion']

        if valor > 2022:
            raise forms.ValidationError("El año de fabricacion no puede ser mayor al año actual")
        return valor


class AutoConcesionarioForm(ModelForm):

    def __init__(self, concesionario, *args, **kwargs):
        super(AutoConcesionarioForm, self).__init__(*args, **kwargs)
        self.initial['concesionario'] = concesionario
        self.fields["concesionario"].widget = forms.widgets.HiddenInput()
        print(concesionario)

    class Meta:
        model = Auto
        fields = ['marca', 'anio_fabricacion', 'valor_minimo', 'valor_maximo', 'color', 'valor_alarma', 'concesionario']
        labels = {
            'anio_fabricacion': _('Año Fabricacion'),
        }   

    def clean_anio_fabricacion(self):
        valor = self.cleaned_data['anio_fabricacion']

        if valor > 2022:
            raise forms.ValidationError("El año de fabricacion no puede ser mayor al año actual")
        return valor

    def clean_valor_maximo(self):
        valor = self.cleaned_data['valor_maximo']
        if (valor) > 100000:
            raise forms.ValidationError("El valor maximo no puede ser mayor a 10000")
        return valor

class MotoConcesionarioForm(ModelForm):

    def __init__(self, concesionario, *args, **kwargs):
        super(MotoConcesionarioForm, self).__init__(*args, **kwargs)
        self.initial['concesionario'] = concesionario
        self.fields["concesionario"].widget = forms.widgets.HiddenInput()
        print(concesionario)

    class Meta:
        model = Moto
        fields = ['marca', 'anio_fabricacion', 'valor_fijo_venta', 'tipo', 'concesionario']
        labels = {
            'anio_fabricacion': _('Año Fabricacion'),
        }   


    def clean_anio_fabricacion(self):
        valor = self.cleaned_data['anio_fabricacion']

        if valor > 2022:
            raise forms.ValidationError("El año de fabricacion no puede ser mayor al año actual")
        return valor





