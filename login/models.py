from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
