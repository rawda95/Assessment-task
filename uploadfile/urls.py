from django.conf.urls import url, include
from django.contrib import admin
from .views import model_form_upload


urlpatterns = [
    url(r'/', model_form_upload , name='model_form_upload'),
]
