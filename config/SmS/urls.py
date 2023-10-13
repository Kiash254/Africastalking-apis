from django.urls import path
from .views import SmsView

app_name='sms'

urlpatterns = [
    path('', SmsView, name='sms'),
]