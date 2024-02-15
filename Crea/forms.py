from django import forms
from .models import *

class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model = Propiedad_posible
        fields = ['codigo', 'fecha_registro', 'ubicacion', 'precio', 'tipo', 'descripcion', 'precio_avaluo', 'id_cliente']