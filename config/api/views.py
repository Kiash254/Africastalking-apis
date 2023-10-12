from django.shortcuts import render
import africastalking
from decouple import config
# Create your views here.

username=config('username')
api_key=config('api_key')

africastalking.initialize(username, api_key)

#ussd service

