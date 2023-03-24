from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):

    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField("email address", blank=False, null=False)
    password = models.CharField("password", max_length=128, blank=False, null=False)
    birthdate = models.DateTimeField("birthdate", blank=True)
    phone = PhoneNumberField(null=True, blank=True)

    REQUIRED_FIELDS = ["email", "password"]
