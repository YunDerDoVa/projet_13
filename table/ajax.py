from django.shortcuts import redirect
from django.http import JsonResponse, Http404
from django.db import IntegrityError

from .models import TablePost, TableLike
from door.models import User


def like_post(request, post_id, like_from_id):
    """ This view add or edit a TableLike object if it exists.
    Today, it redirects to the <GET['next']> value.
    In the future, it will returns a JSON to work with an
    AJAX component. This view sets 'like' field to False. """

    try:
        post = TablePost.objects.get(id=post_id)
        like_from = User.objects.get(id=like_from_id)
    except TablePost.DoesNotExist:
        raise Http404('Post not found...')
    except User.DoesNotExist:
        raise Http404('User not found...')

    like = TableLike.objects.filter(post=post, like_from=like_from).first()
    if like:
        like.edit_like(True)
    else:
        like = post.add_like(like_from)

    json = {
        'success': True,
        'like_id': like.id,
        'like': True,
    }

    return redirect(request.GET['next']+'#post'+str(post.id))

    return JsonResponse(json)


def dislike_post(request, post_id, like_from_id):
    """ This view add or edit a TableLike object if it exists.
    Today, it redirects to the <GET['next']> value.
    In the future, it will returns a JSON to work with an
    AJAX component. This view sets 'like' field to False. """

    try:
        post = TablePost.objects.get(id=post_id)
        like_from = User.objects.get(id=like_from_id)
    except TablePost.DoesNotExist:
        raise Http404('Post not found...')
    except User.DoesNotExist:
        raise Http404('User not found...')

    like = TableLike.objects.filter(post=post, like_from=like_from).first()
    if like:
        like.edit_like(False)
    else:
        like = post.add_like(like_from, dislike=True)

    json = {
        'success': True,
        'like_id': like.id,
        'like': False,
    }

    return redirect(request.GET['next']+'#post'+str(post.id))

    return JsonResponse(json)
