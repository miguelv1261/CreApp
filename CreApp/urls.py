"""
URL configuration for CreApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Crea.views import ver_propiedades_posible, ver_propiedad, index, captar_propiedad, ver_propiedades_disponibles, ver_propiedaddis

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('propiedades_posibles/', ver_propiedades_posible),
    path('propiedades_disponibles/', ver_propiedades_disponibles),
    path('propiedad/<int:codigo_propiedad>/', ver_propiedad ,name="detalle_propiedad"),
    path('propiedaddis/<int:codigo_propiedad>/', ver_propiedaddis ,name="detalle_propiedaddis"),
    path('captar_propiedad/<int:codigo_propiedad>/', captar_propiedad),
]
