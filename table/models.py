from django.db import models
from django.conf import settings


# Create your models here.
class TablePost(models.Model):

    draft = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=None, null=True)
    title = models.CharField(max_length=63, default='')
    description = models.TextField(max_length=2087, default='')
    readme = models.TextField(max_length=2047, null=True)
    script_js = models.FileField(upload_to='scripts_js/', null=True)
    style_css = models.FileField(upload_to='styles_css/')
    private_post = models.BooleanField(default=False)
    number_of_like = models.BigIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def add_like(self, like_from, **kwargs):

        like = not kwargs.pop('dislike', False)
        TableLike.objects.create(like_from=like_from, post=self, like=like)


class TableLike(models.Model):

    like_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(TablePost, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=True)


class TableComment(models.Model):

    comment_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(TablePost, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1023)
    date = models.DateTimeField(auto_now_add=True)
