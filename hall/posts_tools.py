from table.models import TablePost


class DiscoverTool:

    def __init__(self, *models):
        self.models = models

    def get_posts(self):
        return TablePost.objects.all()
