import datetime
from msilib.schema import ListView
from django.shortcuts import redirect, render, redirect , get_object_or_404

from django.core.validators import ValidationError

from django.shortcuts import get_object_or_404, redirect, render

from .models import Propiedad_posible, Propiedad_disponible, P_Cliente, Cliente
from .forms import PropiedadForm , CaptarPropiedadForm, ClienteForm


# Create your views here.

def index(request):
    template = "index.html"
    return render(request, template)

def ver_propiedades_posible(request):
    propiedad = Propiedad_posible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades_posibles.html"
    return render(request, template, contenido)

def nueva_propiedad(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = PropiedadForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_propiedad'] = Propiedad_posible()
    contenido ['form'] = PropiedadForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_propiedad']
    )
    
    return render(request, 'formulario_propiedad.html', contenido)

def editar_propiedad(request, codigo_propiedad):
    contenido = {}
    contenido['propiedad'] = get_object_or_404(Propiedad_posible, pk = codigo_propiedad ) 
    if request.method == 'POST':
        contenido['form'] = PropiedadForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido ['form'] = PropiedadForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['propiedad']
    )
    
    return render(request, 'formulario_propiedad.html', contenido)

def eliminar_propiedad(request, codigo_propiedad):
    contenido = {}
    contenido['propiedad'] = get_object_or_404(Propiedad_posible, pk = codigo_propiedad) 
    contenido['propiedad'].delete()
    return redirect('/propiedades_posibles/')
    
def ver_propiedades_disponibles(request):
    propiedad = Propiedad_disponible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades_disponibles.html"
    return render(request, template, contenido)

def ver_propiedad(request, codigo_propiedad):
    propiedad = get_object_or_404(Propiedad_posible, pk = codigo_propiedad )
    cliente = propiedad.id_cliente
    contenido = {
        'propiedad' : propiedad,
        'cliente': cliente,
    }
    template = "propiedad.html"
    return render(request, template, contenido)

def ver_propiedaddis(request, codigo_propiedad):
    c = {}
    propiedaddis =  get_object_or_404(Propiedad_disponible, pk=codigo_propiedad)
    cliente = propiedaddis.id_cliente
    contenido ={
        'propiedad': propiedaddis,
        'cliente': cliente,
    }
    template = "propiedaddis.html"
    return render(request,template, contenido)



def captar_propiedad(request, codigo_propiedad):
    propiedad = Propiedad_posible.objects.get(pk=codigo_propiedad)

    if request.method == 'POST':
        form = CaptarPropiedadForm(request.POST, instance=propiedad)

        if form.is_valid():
            # Migrar datos y crear nueva instancia en `propiedad_disponible`
            nueva_propiedad = Propiedad_disponible(
                codigo=form.cleaned_data['codigo'],
                fecha_ingreso=datetime.date.today(),  # Set fecha_ingreso to today
                fecha_caducidad=form.cleaned_data.get('fecha_caducidad'),  # Optional field
                tipo=form.cleaned_data['tipo'],
                ubicacion=form.cleaned_data['ubicacion'],
                descripcion=form.cleaned_data['descripcion'],
                tipo_comision=form.cleaned_data['tipo_comision'],
                precio_pactado=form.cleaned_data.get('precio_pactado'),  # Optional field
                precio_comercial=form.cleaned_data['precio_comercial'],
                precio_crea=form.cleaned_data['precio_crea'],
                precio_minimo=form.cleaned_data['precio_minimo'],
                convenio=form.cleaned_data['convenio'],
                proceso='Proceso de Venta',  # Default processo to "Proceso de Venta"
                # Add missing fields if needed (id_cliente, etc.)
            )
            nueva_propiedad.save()
            propiedad.es_activo = False
            propiedad.save()
            return redirect('/propiedades_disponibles')
 
    else:
        form = CaptarPropiedadForm(instance=propiedad)

    context = {
        'form': form,
    }

    return render(request, 'captar_propiedad.html', context)

def ver_pcliente(request):
    cliente = Cliente.objects.all()
    contenido = {
        'cliente' : cliente
    }
    template = "pcliente.html"
    return render(request, template, contenido)

def nuevo_cliente(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = ClienteForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_cliente'] = Cliente()
    contenido ['form'] = ClienteForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_cliente']
    )
    
    return render(request, 'formulario_cliente.html', contenido)

def editar_cliente(request, codigo_cliente):
    contenido = {}
    contenido['cliente'] = get_object_or_404(Cliente, pk = codigo_cliente) 
    if request.method == 'POST':
        contenido['form'] = ClienteForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido ['form'] = ClienteForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['cliente']
    )
    
    return render(request, 'formulario_cliente.html', contenido)

def eliminar_cliente(request, codigo_cliente):
    contenido = {}
    contenido['cliente'] = get_object_or_404(Cliente, pk = codigo_cliente) 
    contenido['cliente'].delete()
    return redirect('/pcliente/')

def ver_pocliente(request, codigo_cliente):


    cliente = get_object_or_404(Cliente, pk = codigo_cliente )


    contenido = {
        "cliente" :cliente,
     
    }
    template = "ppcliente.html"
    return render(request, template, contenido)


