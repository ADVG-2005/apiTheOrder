from django.db import models

# Create your models here.
class Pedido(models.Model):
    peticion = [
        ('pll','Para llevar'),
        ('pco','Para Consumir')
        ]
    nameProduct = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    observacion = models.TextField(max_length=150)
    peticiones = models.CharField(max_length=10,choices=peticion)
    namePedido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.namePedido