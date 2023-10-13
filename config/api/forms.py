from django import forms
from django.forms import ModelForm

from .models import ImageClassification

class ImageClassificationForm(ModelForm):
    class Meta:
        model = ImageClassification
        fields = ['image']