from django.shortcuts import render
from django.http import HttpResponse
import africastalking
# Create your views here.
from .forms import SMSForm

def send_sms(request):
    form = SMSForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # Get the form data
        message = form.cleaned_data['message']
        phone_number = form.cleaned_data['phone_number']

        # Initialize the Africa's Talking API
        username = 'YOUR_USERNAME'
        api_key = 'YOUR_API_KEY'
        africastalking.initialize(username, api_key)

        # Send the SMS message
        sms = africastalking.SMS
        response = sms.send(message, [phone_number])

        # Check if the SMS was sent successfully
        if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
            # SMS was sent successfully
            return HttpResponse('SMS sent successfully')
        else:
            # SMS failed to send
            return HttpResponse('Failed to send SMS')
    else:
        # Render the form
        context = {'form': form}
        return render(request, 'send_sms.html', context)