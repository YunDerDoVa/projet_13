from django.shortcuts import redirect
from django.http import FileResponse, Http404
from django.conf import settings

from .models import TablePost

import os
import tempfile

TEMPDIR = os.path.dirname(os.path.abspath(__file__))


def download_script(request, post_id):
    """ This view returns a FileResponse with the post's script_js field in
    a .js file. """

    try:
        post = TablePost.objects.get(id=post_id)
    except TablePost.DoesNotExist:
        raise Http404('Post not found...')

    filename = 'script_' + str(post.id) + '.js'
    path = settings.MEDIA_ROOT + '\\' + filename
    path = settings.MEDIA_ROOT + '/' + filename

    file = open(path, mode='w+')
    file.write(post.script_js)
    file.close()

    file = open(path, mode='rb')

    response = FileResponse(file, as_attachment=True, filename=filename)

    return response
