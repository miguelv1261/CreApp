from django import forms
from .models import *


class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model = Propiedad_posible
        fields = ['codigo', 'fecha_registro', 'ubicacion', 'precio', 'tipo', 'descripcion', 'precio_avaluo', 'id_cliente']

class CaptarPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad_disponible , Propiedad_posible
        fields = ('codigo', 
                  'fecha_ingreso'=='fecha_registro',
                  'fecha_caducidad'
                  'ubicacion', 
                  'precio_comercial'=='precio', 
                  'tipo',
                  'descripcion',
                  'precio_avaluo',

                  )

