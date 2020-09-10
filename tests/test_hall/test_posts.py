from django.test import TestCase

from door.models import User
from table.models import TablePost
from hall.posts_tools import DiscoverTool
from digitaltesttools.user import create_test_users


class PostsToolTestCase(TestCase):

    def setUp(self):

        user = User.register_new_user(user_dict['username'], user_dict['email'], user_dict['password'])

        TablePost.objects.create(user=user)

    def test_discover_get_posts(self):

        discover_tool = DiscoverTool()

        posts = discover_tool.get_posts()

        self.assertEqual(len(posts), 1)
