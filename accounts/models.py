from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_tour_operator = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


# Create your models here.
