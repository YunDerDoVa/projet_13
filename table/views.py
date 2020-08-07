from django.shortcuts import render

from .views import TablePost, TableLike, TableComment


# Create your views here.
def post(request, post_id):
    post = TablePost.objects.get(id=post_id)

    return render(request, 'table/post.html.django')


def publish(request):
    return render(request, 'table/post.html.django')


def edit(request, post_id):
    post = TablePost.objects.get(id=post_id)

    return render(request, 'table/post.html.django')
