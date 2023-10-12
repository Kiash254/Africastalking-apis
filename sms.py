from flask import Flask
import africastalking

# Set up your credentials
username = "kiash"
api_key = "eef9f7ebbf3d0713809be65c7ec62b6e39d3266c2b2b9f4d4453bb5c4e0b9af5"

# Initialize the Africa's Talking SDK
africastalking.initialize(username, api_key)

# Create a new SMS service
sms = africastalking.SMS

# Create a Flask app
app = Flask(__name__)

# Define the SMS endpoint
@app.route('/sms')
def send_sms():
    # Set the phone number and message
    to_number = '+254712345678'
    message = 'Hello, this is a test message from my Flask app!'

    # Send the SMS using the Africa's Talking SDK
    response = sms.send(message, [to_number])

    # Return the response from the Africa's Talking API
    return str(response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)