from django.test import TestCase
from django.urls import reverse

from digitaltesttools.user import create_test_users


class TableViewsTestCase(TestCase):

    POSTS = [
        ('title0', 'description', 'script.js', 'style.css', False),
        ('title1', 'description', 'script.js', 'style.css', True),
        ('title2', 'description', 'script.js', 'style.css', False),
        ('title3', 'description', 'script.js', 'style.css', True),
        ('title4', 'description', 'script.js', 'style.css', False),
    ]

    def setUp(self) -> None:
        self.test_users = create_test_users(3)

        self.test_posts = []
        for user in self.test_users:
            for POST in self.POSTS:
                post = TablePost.objects.create(
                    user=user,
                    title=POST[0],
                    description=POST[1],
                    script_js=POST[2],
                    style_css=POST[3],
                    private_post=POST[4],
                )
                self.test_posts.append(post)

    def test_post_view(self):
        post = self.test_posts[0]
        url = reverse('table_post', kwargs={'post_id': post.id})
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/post.html.django')

    def test_publish_view(self):
        url = reverse('table_publish')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/publish_post.html.django')

    def test_edit_view(self):
        post = self.test_posts[0]
        url = reverse('table_edit', kwargs={'post_id': post.id})
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'base.html.django')
        self.assertTemplateUsed(response, 'table/edit_post.html.django')