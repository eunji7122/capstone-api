from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    private_key = models.CharField(max_length=100, default=0)
    address = models.CharField(max_length=100, default=0)
