from django.contrib.auth.models import UserManager

from .models import Privacy


class UserManager(UserManager):
    """ Manager of User class. """

    def register_new_user(self, username, email, password):
        """ Create a user and all the attached tables.
        Attached tables list :
        - Privacy
        - (Ergonomy)
        - (Security) """

        user = self.create_user(username=username, email=email, password=password)
        Privacy.objects.create(user=user)

        return user