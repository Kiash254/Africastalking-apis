from django.urls import path
from .views import ussd_callback

app_name = 'api'

urlpatterns = [
    path('', ussd_callback, name='ussd'),
]