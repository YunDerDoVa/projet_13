from django.shortcuts import render, redirect

from .models import TablePost, TableLike
from .forms import PostForm


# Create your views here.
def post(request, post_id):
    table_post = TablePost.objects.get(id=post_id)

    if TableLike.check_liked(table_post, request.user):
        table_post.is_liked = True

    if TableLike.check_disliked(table_post, request.user):
        table_post.is_disliked = True

    context = {
        'post': table_post,
    }

    return render(request, 'table/post.html.django', context)


def publish(request):

    table_post = TablePost(user=request.user)

    form = PostForm(instance=table_post)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            table_post = form.save()

            return redirect('post', post_id=table_post.id)

    context = {
        'form': form,
        'background_instructions': table_post.get_background_instructions()
    }

    return render(request, 'table/publish_post.html.django', context)


def edit(request, post_id):

    table_post = TablePost.objects.get(id=post_id, user=request.user)

    form = PostForm(instance=table_post)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            table_post.title = cd['title']
            table_post.description = cd['description']
            table_post.readme = cd['readme']
            table_post.script_js = cd['script_js']
            table_post.style_css = cd['style_css']
            table_post.private_psot = cd['private_post']

            table_post.save()

            return redirect('post', post_id=post_id)

    context = {
        'form': form,
        'background_instructions': table_post.get_background_instructions()
    }

    return render(request, 'table/edit_post.html.django', context)
