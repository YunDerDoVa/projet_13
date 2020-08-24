from django.shortcuts import render, redirect

from .models import TablePost, TableLike
from .forms import PostForm


# Create your views here.
def post(request, post_id):
    """ This view displays the post in details. """

    table_post = TablePost.objects.get(id=post_id)

    if request.user.is_authenticated:
        if TableLike.check_liked(table_post, request.user):
            table_post.is_liked = True

        if TableLike.check_disliked(table_post, request.user):
            table_post.is_disliked = True

    context = {
        'post': table_post,
    }

    return render(request, 'table/post.html.django', context)


def publish(request):
    """ This view displays a form to create a new post. """

    table_post = TablePost(user=request.user)

    form = PostForm(instance=table_post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=table_post)

        if form.is_valid():
            table_post = form.save()

            return redirect('table_post', post_id=table_post.id)

    context = {
        'form': form,
        'background_instructions': table_post.get_background_instructions()
    }

    return render(request, 'table/publish_post.html.django', context)


def edit(request, post_id):
    """ This view displays a form to edit an existing post. """

    table_post = TablePost.objects.get(id=post_id, user=request.user)

    form = PostForm(instance=table_post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=table_post)

        if form.is_valid():
            form.save()

            return redirect('table_post', post_id=post_id)

    context = {
        'form': form,
        'background_instructions': table_post.get_background_instructions()
    }

    return render(request, 'table/edit_post.html.django', context)
