from django.shortcuts import redirect, render, redirect , get_object_or_404
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
    c['propiedaddis'] =  get_object_or_404(Propiedad_disponible, pk=codigo_propiedad)

    template = "propiedaddis.html"
    return render(request, c)



def captar_propiedad(request, codigo_propiedad):
    c = {}
    c['propiedad'] =  get_object_or_404(Propiedad_posible, pk=codigo_propiedad)
    if request.method == 'POST':
        c['form'] = CaptarPropiedadForm(
                        request.POST or None,
                        request.FILES or None,
                        )
        if c['form'].is_valid():
            c['form'].save()
            return redirect(c['form'].instance.get_absolute_url())
        
    c['form'] = CaptarPropiedadForm(
        request.POST or None,
        request.FILES or None,
        instance = c['propiedad']
    )
    return render(request, 'captar_propiedad.html', c)

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
    contenido['cliente'] = get_object_or_404(Cliente, pk = codigo_cliente ) 
    contenido['cliente'].delete()
    return redirect('/pcliente/')

def ver_pocliente(request, codigo_cliente):
    pcliente = Cliente.objects.get(pk = codigo_cliente )
    contenido = {
        "pcliente" :pcliente
    }
    template = "ppcliente.html"
    return render(request, template, contenido)