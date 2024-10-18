from rest_framework.routers import DefaultRouter
from apps.pedido.api.views import PedidoViewSet

router_pedido = DefaultRouter()
router_pedido.register(prefix='pedidos',viewset=PedidoViewSet)