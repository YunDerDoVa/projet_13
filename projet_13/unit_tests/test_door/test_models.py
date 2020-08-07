from django.test import TestCase
from django.contrib.auth import authenticate
from django.db import models

from digitaltesttools.user import get_user_dict
from door.models import User


# Create your tests here.
class DoorModelsTestCase(TestCase):

    def setUp(self) -> None:
        user_dict = get_user_dict(0)
        user = User.register_new_user(user_dict['username'], user_dict['email'], user_dict['password'])

        self.user_dict = user_dict
        self.user = user

    def test_register_new_user(self):
        user_dict = self.user_dict
        user = User.objects.get(username=user_dict['username'], email=user_dict['email'])

        self.assertTrue(user is not None)
        self.assertEqual(user.username, user_dict['username'])
        self.assertEqual(user.email, user_dict['email'])

    def test_authenticate_user(self):
        user_dict = self.user_dict
        user = authenticate(username=self.user_dict['username'], password=self.user_dict['password'])

        self.assertTrue(user is not None)
        self.assertEqual(user.username, user_dict['username'])
        self.assertEqual(user.email, user_dict['email'])

    def test_user_fields(self):
        user = User.objects.first()

        self.assertTrue('avatar' in user.__dict__.keys())
        self.assertTrue('banner' in user.__dict__.keys())
