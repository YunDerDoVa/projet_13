from django.shortcuts import redirect
from django.http import JsonResponse
from django.db import IntegrityError

from .models import TablePost, TableLike
from door.models import User


def like_post(request, post_id, like_from_id):

    post = TablePost.objects.get(id=post_id)
    like_from = User.objects.get(id=like_from_id)

    try:
        like = TableLike.objects.create(post=post, like_from=like_from)
    except IntegrityError:
        like = TableLike.objects.get(post=post, like_from=like_from)
        like.like = True
        like.save()

    json = {
        'success': True,
        'like_id': like.id,
        'like': True,
    }

    return redirect(request.GET['next']+'#post'+str(post.id))

    return JsonResponse(json)


def dislike_post(request, post_id, like_from_id):
    post = TablePost.objects.get(id=post_id)
    like_from = User.objects.get(id=like_from_id)

    try:
        like = TableLike.objects.create(post=post, like_from=like_from, like=False)
    except IntegrityError:
        like = TableLike.objects.get(post=post, like_from=like_from)
        like.like = False
        like.save()

    json = {
        'success': True,
        'like_id': like.id,
        'like': False,
    }

    return redirect(request.GET['next']+'#post'+str(post.id))

    return JsonResponse(json)