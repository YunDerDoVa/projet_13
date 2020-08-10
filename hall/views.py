from django.shortcuts import render

from door.models import User
from .posts_tools import DiscoverTool


# Create your views here.
def index(request):
    """ index view render the landing home page """

    number_of_users = User.objects.count()

    context = {
        'number_of_users': number_of_users,
    }

    return render(request, 'hall/index.html.django', context)


def discover(request):

    discover_tool = DiscoverTool()

    posts = discover_tool.get_posts()

    context = {
        'posts': posts,
    }

    return render(request, 'hall/discover.html.django', context)
