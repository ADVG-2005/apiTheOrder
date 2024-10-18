from rest_framework.viewsets import ModelViewSet
from apps.pedido.models import Pedido
from apps.pedido.serializers import PedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ['get','post','patch']