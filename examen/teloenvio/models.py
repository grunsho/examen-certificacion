from django.db import models

# Create your models here.
class Productor(models.Model):
    idProductor = models.AutoField(primary_key=True)
    nombreContacto = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    razonSocial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreContacto
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=25)
    descripcionProducto = models.TextField(blank=True)
    precioProducto = models.PositiveIntegerField()
    imagenProducto = models.ImageField(upload_to='productos/')
    stockProducto = models.PositiveIntegerField()
    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    fono = models.CharField(max_length=10)
    identificador = models.CharField(max_length=20)
    numIdentificador = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Pedido(models.Model):
    METODOPAGO_CHOICES = [
        ('TF', 'Transferencia'),
        ('TC', 'Tarjeta de Crédito'),
        ('TD', 'Tarjeta de Débito')
    ]
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('En Despacho', 'En Despacho'),
        ('Entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaPedido = models.DateField(auto_now_add=True)
    direccionEntrega = models.CharField(max_length=100)
    estadoPedido = models.CharField(choices=ESTADO_CHOICES, default='Pendiente')
    formaPago = models.CharField(choices=METODOPAGO_CHOICES)
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()