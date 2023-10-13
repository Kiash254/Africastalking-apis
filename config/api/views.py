from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from decouple import config
# Initialize Africa's Talking
image_classifications = config('image_classifications')


   