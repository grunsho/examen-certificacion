from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('agregar_producto', AgregarProducto.as_view(), name="agregar_producto"),
    path('gestion_productos', GestionProductosView.as_view(), name='gestion_productos'),
    path('crear_productor', CrearProductorView.as_view(), name='crear_productor'),
    path('crear_pedido', CrearPedidoView.as_view(), name='crear_pedido'),
    path('gestion_pedidos', GestionPedidosView.as_view(), name='gestion_pedidos'),
    path('detalle_pedido', DetallePedidoView.as_view(), name='detalle_pedido'),
]