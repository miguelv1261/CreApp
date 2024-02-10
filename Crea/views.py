from django.shortcuts import redirect, render
from .models import Propiedad_posible, CaptarPropiedadForm, Propiedad_disponible, P_Cliente


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

def ver_propiedades_disponibles(request):
    propiedad = Propiedad_disponible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades_disponibles.html"
    return render(request, template, contenido)

def ver_propiedad(request, codigo_propiedad):
    propiedad = Propiedad_posible.objects.get(pk = codigo_propiedad )
    cliente = propiedad.id_cliente
    contenido = {
        'propiedad' : propiedad,
        'cliente': cliente,
    }
    template = "propiedad.html"
    return render(request, template, contenido)

def ver_propiedaddis(request, codigo_propiedad):
    propiedad = Propiedad_disponible.objects.get(pk = codigo_propiedad )
    cliente = propiedad.id_cliente
    contenido = {
        'propiedad' : propiedad,
        'cliente': cliente,
    }
    template = "propiedaddis.html"
    return render(request, template, contenido)

def captar_propiedad(request, codigo_propiedad):
    propiedad = Propiedad_posible.objects.get(pk=codigo_propiedad)

    if request.method == 'POST':
        form = CaptarPropiedadForm(request.POST)

        if form.is_valid():
            form.save()

            # Eliminar la instancia de la tabla propiedades_posibles
            

            return redirect('/propiedades_disponibles')
    else:
        form = CaptarPropiedadForm(instance=propiedad)

    context = {
        'form': form,
    }

    return render(request, 'captar_propiedad.html', context)

def ver_pcliente(request):
    pcliente = P_Cliente.objects.all()
    contenido = {
        'pcliente' : pcliente
    }
    template = "pcliente.html"
    return render(request, template, contenido)

def ver_pocliente(request, codigo_cliente):
    pcliente = P_Cliente.objects.get(pk = codigo_cliente )
    contenido = {
        "pcliente" :pcliente
    }
    template = "ppcliente.html"
    return render(request, template, contenido)