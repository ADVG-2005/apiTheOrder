from django.db import models
from apps.pedido.models import Pedido

# Create your models here.
class Factura(models.Model):
    fecha = models.DateField(auto_now=True)
    pedido = models.ForeignKey(Pedido,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.fecha