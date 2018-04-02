from django.conf.urls import url, include
from rest_framework import routers

from .views import PlaceViewSet, RateViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'rate', RateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
