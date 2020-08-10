from table.models import TablePost


class DiscoverTool:
    """ This package is a suite of tools to interact with the
    table django app. """

    def __init__(self, *models):
        self.models = models

    def get_posts(self):
        """ This method return TablePost queryset. Order it randomly
        and reorder it with a simple algorithm. """

        return TablePost.objects.all()
