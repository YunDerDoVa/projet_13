from django.test import TestCase

from digitaltesttools.user import create_test_users
from table.models import TablePost, TableLike, TableComment


class TableModelsTestCase(TestCase):

    POSTS = [
        ('title0', 'description', 'script.js', 'style.css', False),
        ('title1', 'description', 'script.js', 'style.css', True),
        ('title2', 'description', 'script.js', 'style.css', False),
        ('title3', 'description', 'script.js', 'style.css', True),
        ('title4', 'description', 'script.js', 'style.css', False),
    ]

    COMMENTS = [
        'Super !',
        'Je commente ici.',
        'Test comm\'...',
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

    def test_table_post(self):
        user = self.test_users[0]
        post = TablePost.objects.filter(user=user).first()

        self.assertEqual(post.user, user)
        self.assertTrue(post.creation_date is not None)
        self.assertTrue(post.last_update_date is not None)
        self.assertEqual(post.number_of_like, 0)

    def test_table_post_add_like_function(self):
        user_post = self.test_users[0]
        user_like = self.test_users[1]
        post = TablePost.objects.filter(user=user_post).first()

        post.add_like(user_like)
        like = TableLike.objects.get(like_from=user_like, post=post)

        self.assertEqual(post.number_of_like, 1)
        self.assertEqual(post.table_like_set.count(), 1)
        self.assertEqual(like, post.table_like_set.first())
        self.assertTrue(post.table_like_set.first().like)

    def test_table_like(self):
        user_like = self.test_users[2]
        post = self.test_posts[0]
        like = TableLike.objects.create(like_from=user_like, post=post)

        self.assertEqual(like.like_from, user_like)
        self.assertEqual(like.post, post)
        self.assertTrue(like.like)

    def test_table_comment(self):
        str_comment = self.COMMENTS[0]

        user_post = self.test_users[0]
        user_comment = self.test_users[1]
        post = TablePost.objects.filter(user=user_post).first()
        comment = TableComment.objects.create(post=post, comment_from=user_comment, comment=str_comment)

        self.assertEqual(comment.comment, str_comment)
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.comment_from, user_comment)
