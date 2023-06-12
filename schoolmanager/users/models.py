from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """A custom user model for extension"""
    pass

