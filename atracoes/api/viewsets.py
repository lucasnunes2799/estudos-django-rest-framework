from rest_framework.viewsets import ModelViewSet
from .serializers import AtracaoSerializer
from atracoes.models import Atracao

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer