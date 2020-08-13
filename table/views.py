from django.shortcuts import render, redirect

from .models import TablePost, TableLike, TableComment
from .forms import PostForm


# Create your views here.
def post(request, post_id):
    table_post = TablePost.objects.get(id=post_id)

    context = {
        'post': table_post,
    }

    return render(request, 'table/post.html.django', context)


def publish(request):

    table_post = TablePost(user=request.user)

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            table_post = form.save()
            return redirect('post', post_id=table_post)

    context = {
        'form': form,
        'background_instructions': table_post.get_background_instructions()
    }

    return render(request, 'table/publish_post.html.django', context)


def edit(request, post_id):
    table_post = TablePost.objects.get(id=post_id)

    context = {
        'post': table_post,
    }

    return render(request, 'table/edit_post.html.django', context)
