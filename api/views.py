from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Place, Rate
from .serializers import PlaceSerializer, RateSerializer


# Create your views here.
class PlaceViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class RateViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
