# views.py
from django.http import HttpResponse
from django.shortcuts import render
from decouple import config
import requests  # Import the requests library

# Fetch the image classification API key from the .env file
image_classifications = config('image_classifier')

# Define your image classification API endpoint
api_endpoint = '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'  # Replace with your API URL

def classify_image(image):
    try:
        # Prepare a POST request to your image classification API
        files = {'image': image}
        headers = {'Authorization': f'Bearer {image_classifications}'}

        # Send the image to the image classification API
        response = requests.post(api_endpoint, headers=headers, files=files)

        if response.status_code == 200:
            # If the request was successful, return the classification result
            return response.text
        else:
            # If the request was not successful, handle the error
            return f'Error: {response.status_code} - {response.text}'
    except Exception as e:
        return f'Error: {str(e)}'

def image_classification(request):
    if request.method == 'POST':
        # Get the image from the request
        image = request.FILES.get('image')
        
        # Call the classify_image function to send the image to the API and get the result
        result = classify_image(image)

        # Return the result to the user
        return HttpResponse(f'Image classification result: {result}')
    return render(request, 'upload_image.html')  # You should have an HTML template for uploading images
