from django import forms
from .models import *

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
