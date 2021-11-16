from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer