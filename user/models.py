from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    email = models.EmailField("email address", blank=False, null=False, unique=True)
    birthdate = models.DateTimeField("birthdate", blank=True, null=True)
    phone = PhoneNumberField("phone", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]
