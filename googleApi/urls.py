from django.conf.urls import url
from .views import distance_matrix

app_name = 'google-api'

urlpatterns = [
    url(r'^distance/', distance_matrix,name='distance_matrix'),

]