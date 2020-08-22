from django.shortcuts import render

from door.models import User
from .posts_tools import DiscoverTool
from table.models import TableLike


# Create your views here.
def index(request):
    """ index view render the landing home page """

    number_of_users = User.objects.all().count()

    context = {
        'number_of_users': number_of_users,
    }

    return render(request, 'hall/index.html.django', context)


def discover(request):

    discover_tool = DiscoverTool()

    posts = discover_tool.get_posts()

    for post in posts:
        if TableLike.check_liked(post, request.user):
            post.is_liked = True

        if TableLike.check_disliked(post, request.user):
            post.is_disliked = True

    context = {
        'posts': posts,
    }

    return render(request, 'hall/discover.html.django', context)
