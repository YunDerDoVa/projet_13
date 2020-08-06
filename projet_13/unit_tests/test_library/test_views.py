from django.test import TestCase
from django.urls import reverse

from digitaltesttools.user import create_test_users


class LibraryViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.test_users = create_test_users(3)

    def test_library_view(self):
        url = reverse('library')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'library/dashboard.html.django')