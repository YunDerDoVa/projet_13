from django.test import TestCase, Client
from django.urls import reverse

from digitaltesttools.user import create_test_users, get_or_create_test_users
from digitaltesttools.user import TEST_PASSWORD
from table.models import TablePost


class TableViewsTestCase(TestCase):

    POSTS = [
        ('title0', 'description', 'script.js', False),
        ('title1', 'description', 'script.js', True),
        ('title2', 'description', 'script.js', False),
        ('title3', 'description', 'script.js', True),
        ('title4', 'description', 'script.js', False),
    ]

    def setUp(self) -> None:
        self.client = Client()

        self.test_users = get_or_create_test_users(3)

        self.test_posts = []
        for user in self.test_users:
            for POST in self.POSTS:
                post = TablePost.objects.create(
                    user=user,
                    title=POST[0],
                    description=POST[1],
                    script_js=POST[2],
                    private_post=POST[3],
                )
                self.test_posts.append(post)

    def test_post_view(self):
        post = self.test_posts[0]
        url = reverse('table_post', kwargs={'post_id': post.id})
        self.client.login(username=post.user.username, password=TEST_PASSWORD)
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/post.html.django')

    def test_publish_view(self):
        url = reverse('table_publish')
        self.client.login(
            username=self.test_users[1].username,
            password=TEST_PASSWORD)
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/publish_post.html.django')

    def test_edit_view(self):
        post = self.test_posts[0]
        url = reverse('table_edit', kwargs={'post_id': post.id})
        self.client.login(username=post.user.username, password=TEST_PASSWORD)
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/edit_post.html.django')
