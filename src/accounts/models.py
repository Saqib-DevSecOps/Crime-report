from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=30)
    username = models.CharField(max_length=30)
    REQUIRED_FIELDS = ['username', ]
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + self.last_name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(upload_to='user/profile')
    phone_no = models.CharField(max_length=30)
    country = CountryField()
    city = models.CharField(max_length=30, null=True, blank=False)
    address = models.CharField(max_length=150, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
