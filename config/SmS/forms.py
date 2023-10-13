from django import forms

class SmsForm(forms.Form):
    message = forms.CharField(label='Message', max_length=160)
    phone_number = forms.CharField(label='Phone Number', max_length=10)