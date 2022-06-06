from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(default='user', max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
