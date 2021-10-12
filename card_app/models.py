from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Card(models.Model):
    photo = models.ImageField(upload_to='media', default='defaultphoto.jpg', blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    avenue = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
