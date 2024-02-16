from django import forms
from .models import *
class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model = Propiedad_posible
        fields = ['codigo', 'fecha_registro', 'ubicacion', 'precio', 'tipo', 'descripcion', 'precio_avaluo', 'id_cliente']

class CaptarPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad_disponible 
        fields = ('codigo', 
                  'fecha_ingreso',
                  'fecha_caducidad',
                  'ubicacion', 
                  'precio_comercial', 
                  'tipo',
                  'descripcion',
                  )
        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula', 'telefono', 'correo', 'observaciones']
