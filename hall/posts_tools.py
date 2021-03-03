from table.models import TablePost


class DiscoverTool:
    """ This package is a suite of tools to interact with the
    table django app. """

    def __init__(self, *models):
        self.models = models

    def get_posts(self):
        """ This method return TablePost queryset. Order it randomly
        and reorder it with a simple algorithm. """

        posts = TablePost.objects.order_by('-creation_date').filter(
            private_post=False, user__privacy_settings__private_posts=False).all()

        posts = posts[:7]

        return posts
