from django.test import TestCase
from django.urls import reverse

from digitaltesttools.user import create_test_users


class HallViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.test_users = create_test_users(3)

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'hall/index.html.django')

    def test_discover_view(self):
        url = reverse('discover')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'hall/discover.html.django')