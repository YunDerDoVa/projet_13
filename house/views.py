from django.shortcuts import render


from table.models import TablePost, TableLike
from door.models import User


# Create your views here.
def dashboard(request):

    context = {
        'user': request.user,
    }

    return render(request, 'house/dashboard.html.django', context)


def my_library(request):

    posts = TablePost.objects.filter(user=request.user).all()

    context = {
        'posts': posts,
    }

    return render(request, 'house/my_library.html.django', context)


def my_likes(request):

    likes = TableLike.objects.filter(like_from=request.user).all()

    context = {
        'likes': likes,
    }

    return render(request, 'house/my_likes.html.django', context)


def living_room(request, user_id):

    user = User.objects.get(id=user_id)

    posts = TablePost.objects.filter(user=user)

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'house/living_room.html.django', context)
