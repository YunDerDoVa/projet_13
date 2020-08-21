from django.shortcuts import redirect
from django.http import FileResponse
from django.conf import settings

from .models import TablePost

import os
import tempfile

TEMPDIR = os.path.dirname(os.path.abspath(__file__))


def download_script(request, post_id):
    post = TablePost.objects.get(id=post_id)

    filename = 'script_' + str(post.id) + '.js'
    path = settings.MEDIA_ROOT + '\\' + filename
    path = settings.MEDIA_ROOT + '/' + filename

    file = open(path, mode='w+')
    file.write(post.script_js)
    file.close()

    file = open(path, mode='rb')

    response = FileResponse(file)

    return response
