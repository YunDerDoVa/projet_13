from django.test import TestCase
from django.urls import reverse

from digitaltesttools.user import create_test_users


class HouseViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.test_users = create_test_users(3)

    def test_dashboard_view(self):
        url = reverse('dashboard')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/dashboard.html.django')

    def test_my_library_view(self):
        url = reverse('my_library')
        self.client.login(username=self.test_users[0].username, password=self.test_users[0].password)
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/my_library.html.django')

    def test_my_likes_view(self):
        url = reverse('my_likes')
        self.client.login(username=self.test_users[1].username, password=self.test_users[1].password)
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/my_likes.html.django')