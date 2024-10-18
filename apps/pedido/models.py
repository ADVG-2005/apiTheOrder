from django.db import models
from apps.producto.models import Producto
# Create your models here.
class Pedido(models.Model):
    peticion = [
        ('pll','Para llevar'),
        ('pco','Para Consumir')
        ]
    estado_preparacion =[
        ('esp','En espera'),
        ('pre','En preparacion'),
        ('ser','Servido')
    ]
    nameProduct = models.ForeignKey(Producto,on_delete=models.SET_NULL,null=True)
    cantidad = models.IntegerField()
    observacion = models.TextField(max_length=150)
    peticiones = models.CharField(max_length=10,choices=peticion)
    estado = models.CharField(max_length=10, choices=estado_preparacion)
    namePedido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.namePedido