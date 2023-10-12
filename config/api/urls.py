from django.urls import path
from .views import Ussd

app_name = 'api'

urlpatterns = [
    path('ussd/', Ussd.as_view(), name='ussd'),
]