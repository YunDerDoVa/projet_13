from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class Privacy(models.Model):
    """ Privacy settings model. """

    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, related_name='privacy_settings')
    private_profile = models.BooleanField(default=False)
    private_posts = models.BooleanField(default=False)

    disable_account = models.DateField(null=True, default=None, blank=True)


class User(AbstractUser):
    """ User with more options. """

    BANNER_CHOICES = [
        (0, 'Dev Mode'),
        (1, 'Unsplash Random'),
    ]

    avatar = models.ImageField(upload_to='user/')
    banner = models.IntegerField(default=0, choices=BANNER_CHOICES)

    @staticmethod
    def register_new_user(username, email, password):
        """ Create a user and all the attached tables.
        Attached tables list :
        - Privacy
        - (Ergonomy)
        - (Security) """

        user = User.objects.create_user(username=username, email=email, password=password)
        Privacy.objects.create(user=user)

        return user
