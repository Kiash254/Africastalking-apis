from django.db import models

# Create your models here.

class ImageClassification(models.Model):
    image = models.ImageField(upload_to='images/')
    image_classification = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)