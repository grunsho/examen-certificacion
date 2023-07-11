import contextlib
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Cliente, Producto, Productor, Pedido, DetallePedido
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AgregarProducto(CreateView):
    template_name = 'agregar_producto.html'
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('gestion_productos')

class GestionProductosView(View):
    template_name = 'gestion_productos.html'
    
    def get(self, request):
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, self.template_name, context)

class CrearProductorView(CreateView):
    template_name = 'crear_productor.html'
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('index')

class CrearPedidoView(CreateView):
    template_name = "crear_pedido.html"
    model = Pedido
    fields = '__all__'
    success_url = 'gestion_pedidos'

class GestionPedidosView(View):
    template_name = 'gestion_pedidos.html'

    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        context = {'pedidos': pedidos}
        return render(request, self.template_name, context=context)

class DetallePedidoView(DetailView):
    template_name = 'detalle_pedido.html'
    model = DetallePedido
    
