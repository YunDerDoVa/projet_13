from django.shortcuts import render


from table.models import TablePost, TableLike
from door.models import User


# Create your views here.
def dashboard(request):
    """ The dashboard displays some buttons to navigate into our personal
    space. (our house) """

    context = {
        'user': request.user,
    }

    return render(request, 'house/dashboard.html.django', context)


def my_library(request):
    """ The 'my_library' view displays all scripts we posted on the website. """

    posts = TablePost.objects.filter(user=request.user).all()

    context = {
        'posts': posts,
    }

    return render(request, 'house/my_library.html.django', context)


def my_likes(request):
    """ The 'my_likes' view displays all posts we liked on the website. """

    posts = TablePost.objects.filter(table_like_set__like_from=request.user,
        table_like_set__like=True)

    for post in posts:
        post.is_liked = True

    context = {
        'posts': posts,
    }

    return render(request, 'house/my_likes.html.django', context)


def living_room(request, user_id):
    """ The living_room is like the 'Facebook wall'. All your publics
    activities are visible on the page. """

    user = User.objects.get(id=user_id)

    posts = TablePost.objects.filter(user=user)

    if request.user.is_authenticated:
        for post in posts:
            if TableLike.check_liked(post, request.user):
                post.is_liked = True

            if TableLike.check_disliked(post, request.user):
                post.is_disliked = True

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'house/living_room.html.django', context)
