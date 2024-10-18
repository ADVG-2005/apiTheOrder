from rest_framework.viewsets import ModelViewSet
from apps.factura.models import Factura
from apps.factura.serializers import FacturaSerializer

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer