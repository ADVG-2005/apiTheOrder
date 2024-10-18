from rest_framework.routers import DefaultRouter
from apps.producto.api.views import ProductoViewSet

router = DefaultRouter()
router.register(prefix='productos',viewset=ProductoViewSet)