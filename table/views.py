from django.shortcuts import render

from .models import TablePost, TableLike, TableComment


# Create your views here.
def post(request, post_id):
    post = TablePost.objects.get(id=post_id)

    context = {
        'post': post,
    }

    return render(request, 'table/post.html.django', context)


def publish(request):
    return render(request, 'table/post.html.django')


def edit(request, post_id):
    post = TablePost.objects.get(id=post_id)

    context = {
        'post': post,
    }

    return render(request, 'table/post.html.django', context)
