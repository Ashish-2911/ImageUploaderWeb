from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager  import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.EmailField(max_length=30 , blank=True)
    last_name = models.CharField(max_length=30 , blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.EmailField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email