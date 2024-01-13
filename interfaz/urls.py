"""
URL configuration for interfaz project.

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
from appi.views import home

from appi.views import registrarCliente
from appi.views import editar_cliente
from appi.views import eliminar_cliente
from appi.views import listar_clientes
from appi.views import registrar_producto
from appi.views import editar_producto
from appi.views import eliminar_producto
from appi.views import listar_productos
from appi.views import registrar_factura
from appi.views import editar_factura
from appi.views import eliminar_factura
from appi.views import listar_facturas
from appi.views import mas_vendidos
from appi.views import listar_topClientes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="principal"),
    path('home/',home,name="home"),
    path('editar-cliente/', editar_cliente, name='editar_cliente'),
    ##Funcion para registrar los clientes
    path('registrar-cliente/', registrarCliente, name='registrar_cliente'),
    path('eliminar-cliente/', eliminar_cliente, name='eliminar_cliente'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),
    ##Funcion para registrar los productos
    path('registrar-producto/', registrar_producto, name='registrar_producto'),
    path('editar-producto/', editar_producto, name='editar_producto'),
    path('eliminar-producto/', eliminar_producto, name='eliminar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    ##Funcion para registrar las facturas
    path('registrar-factura/', registrar_factura, name='registrar_factura'),
    path('editar-factura/', editar_factura, name='editar_factura'),
    path('eliminar-factura/', eliminar_factura, name='eliminar_factura'),
    path('listar-facturas/', listar_facturas, name='listar_facturas'),
    path('mas_vendidos/', mas_vendidos, name='productos_mas_vendidos'),
    path('listar-topClientes/', listar_topClientes, name='top_clientes')
]

