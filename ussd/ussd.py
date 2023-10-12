import africastalking

# Set up your credentials
username = "kiash"
api_key = "0804fc11a4dbeb6dbe78fafa7bd337e16f49271c7ab33854f3c4572d5d80a4e1"

# Initialize the Africa's Talking SDK
africastalking.initialize(username, api_key)

# Define the USSD handler function
def ussd_handler(request):
    # Get the user's input
    user_input = request.values.get("text", "")
    
    # Define the USSD response
    if user_input == "":
        response = "CON Welcome to my USSD app. Please enter your name:"
    elif user_input != "":
        response = "END Thank you for using my USSD app, {}!".format(user_input)
    
    # Return the USSD response
    return response

# Create a new USSD application
app = africastalking.USSD()

# Attach the USSD handler function to the application
app.set_response_handler(ussd_handler)

# Start the USSD application
app.start(port=5000)
