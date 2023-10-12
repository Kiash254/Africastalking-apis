from flask import Flask, request
import africastalking

# Initialize Flask app
app = Flask(__name__)

# Initialize Africastalking API
username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Define route for sending SMS
@app.route('/send_sms', methods=['POST'])
def send_sms():
    # Get phone number and message from request
    phone_number = request.form['phone_number']
    message = request.form['message']

    # Send SMS using Africastalking API
    response = sms.send(message, [phone_number])

    # Return response from API
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
