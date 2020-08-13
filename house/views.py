from django.shortcuts import render


from table.models import TablePost, TableLike


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html.django')


def my_library(request):

    posts = TablePost.objects.filter(user=request.user).all()

    context = {
        'posts': posts,
    }

    return render(request, 'my_library.html.django', context)


def my_likes(request):

    likes = TableLike.objects.filter(like_from=request.user).all()

    context = {
        'likes': likes,
    }

    return render(request, 'my_likes.html.django', context)
