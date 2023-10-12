from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking
from decouple import config

# Initialize Africa's Talking
username = config('USERNAME')
api_key = config('API_KEY')
africastalking.initialize(username, api_key)

# Define the USSD handler function
@csrf_exempt
def ussd_callback(request):
    # Get the POST parameters
    session_id = request.POST.get('sessionId')
    phone_number = request.POST.get('phoneNumber')
    service_code = request.POST.get('serviceCode')
    text = request.POST.get('text')

    # Split the text into an array of strings
    text_array = text.split('*')

    # Get the user's response
    user_response = text_array[-1]

    # Define the USSD menu
    menu = 'CON Welcome to My USSD App\n'
    menu += '1. Check balance\n'
    menu += '2. Buy airtime\n'
    menu += '3. Transfer money\n'

    # Handle the user's response
    if user_response == '':
        # User is at the main menu
        response = menu
    elif user_response == '1':
        # User wants to check balance
        response = 'END Your balance is KES 1000\n'
    elif user_response == '2':
        # User wants to buy airtime
        response = 'CON Enter amount\n'
    elif user_response.startswith('2*'):
        # User has entered the airtime amount
        amount = text_array[-1]
        response = 'END You have bought KES {} airtime\n'.format(amount)
    elif user_response == '3':
        # User wants to transfer money
        response = 'CON Enter recipient phone number\n'
    elif user_response.startswith('3*'):
        # User has entered the recipient phone number
        recipient = text_array[-1]
        response = 'CON Enter amount\n'
    elif user_response.startswith('3*'):
        # User has entered the transfer amount
        amount = text_array[-1]
        response = 'END You have transferred KES {} to {}\n'.format(amount, recipient)
    else:
        # Invalid input
        response = 'END Invalid input\n'

    # Return the USSD response
    return HttpResponse(response)