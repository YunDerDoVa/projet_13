from django.test import TestCase
from django.urls import reverse


from digitaltesttools.user import create_test_users


# Create your tests here.
class DoorViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.test_users = create_test_users(3)

    def test_login_view(self):
        url = reverse('login_view')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'door/base.html.django')
        self.assertTemplateUsed(response, 'door/login.html.django')

    def test_register_view(self):
        url = reverse('register_view')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'door/base.html.django')
        self.assertTemplateUsed(response, 'door/register.html.django')