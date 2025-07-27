from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    native_language = models.CharField(max_length=30, blank=True, null=True)
    learning_language = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
