from django import forms
from .models import Producto, Productor, Cliente, Pedido, DetallePedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto', 'descripcionProducto', 'precioProducto', 'stockProducto', 'idProductor']
        labels = {
            'nombreProducto': 'Nombre',
            'descripcionProducto': 'Descripción',
            'precioProducto': 'Precio',
            'stockProducto': 'Stock actual',
            'idProductor': 'ID Productor'
        }
        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcionProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'precioProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'stockProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'idProductor': forms.Select(attrs={'class': 'form-control'}),
        }

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccionEntrega', 'estadoPedido', 'formaPago']
        labels = {
            'cliente': 'Cliente',
            'fechaPedido': 'Fecha de pedido',
            'direccionEntrega': 'Dirección de entrega',
            'estadoPedido': 'Estado del pedido',
            'formaPago': 'Forma de pago'
        }
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaPedido': forms.DateInput(attrs={'class': 'form-control'}, format=('%d/%m/%Y')),
            'direccionEntrega': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoPedido': forms.Select(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
        }