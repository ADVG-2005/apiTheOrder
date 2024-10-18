from django.db import models
from apps.pedido.models import Pedido

# Create your models here.
class Preparacion(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.SET_NULL,null=True)
    cantidad = 