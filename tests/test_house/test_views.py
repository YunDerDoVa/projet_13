from django.test import TestCase
from django.urls import reverse

from digitaltesttools.user import get_or_create_test_users
from digitaltesttools.user import TEST_PASSWORD


class HouseViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.test_users = get_or_create_test_users(3)
        self.client.login(
            username=self.test_users[0].username,
            password=TEST_PASSWORD)

    def test_dashboard_view(self):
        url = reverse('dashboard')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/dashboard.html.django')

    def test_my_library_view(self):
        url = reverse('my_library')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/my_library.html.django')

    def test_my_likes_view(self):
        url = reverse('my_likes')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'house/my_likes.html.django')
