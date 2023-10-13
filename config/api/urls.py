from django.urls import path
from .views import image_classification

app_name = 'api'

urlpatterns = [
    path('',image_classification, name='ussd'),
]