from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


# Create your models here.
class Privacy(models.Model):
    """ Privacy settings model. """

    private_profile = models.BooleanField(default=False)
    private_posts = models.BooleanField(default=False)


class User(AbstractUser):
    """ User with more options. """

    avatar = models.ImageField(upload_to='user/')
    banner = models.IntegerField(default=0)
    privacy_settings = models.OneToOneField(Privacy, on_delete=models.SET_NULL, null=True)

    objects = UserManager()
