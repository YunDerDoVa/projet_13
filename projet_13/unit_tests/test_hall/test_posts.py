from django.test import TestCase

from hall.posts_tools import DiscoverTool


class PostsToolTestCase(TestCase):

    def test_discover_get_posts(self):

        discover_tool = DiscoverTool()

        posts = discover_tool.get_posts()

        self.assertEqual(len(posts), 1)
