from django.test import TestCase

from table.models import TablePost
from hall.posts_tools import DiscoverTool
from digitaltesttools.user import create_test_users


class PostsToolTestCase(TestCase):

    def setUp(self):

        user = create_test_users(1)[0]

        TablePost.objects.create(user=user)

    def test_discover_get_posts(self):

        discover_tool = DiscoverTool()

        posts = discover_tool.get_posts()

        self.assertEqual(len(posts), 1)
