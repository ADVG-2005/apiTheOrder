from rest_framework.viewsets import ModelViewSet
from apps.producto.models import Producto
from apps.producto.serializers import ProductoSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer