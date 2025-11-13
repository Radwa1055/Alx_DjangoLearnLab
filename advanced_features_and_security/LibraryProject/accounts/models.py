from django import abstractUser
from django.db import models

class CustomUser(abstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
    