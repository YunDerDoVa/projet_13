from django.test import TestCase

from digitaltesttools.user import create_test_users
from table.models import TablePost, TableLike


class TableModelsTestCase(TestCase):

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

    def test_table_post(self):
        user = self.test_users[0]
        post = TablePost.objects.filter(user=user).first()

        self.assertEqual(post.user, user)
        self.assertTrue(post.date_creation is not None)
        self.assertTrue(post.date_last_update is not None)
        self.assertEqual(post.number_of_likes, 0)

    def test_add_like_function(self):
        user_liked = self.test_users[0]
        user_liker = self.test_users[1]
        post = TablePost.objects.filter(user=user_liked).first()

        post.add_like(user_liker, dislike=True)

        self.assertEqual(post.number_of_likes, 1)
        self.assertEqual(post.like_set.count(), 1)
        self.assertEqual(TableLike.objects.get(from=user_liker,to=user_liked, post=post), post.like_set.first())
        self.assertFalse(post.like_set.first())
