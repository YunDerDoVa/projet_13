from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.
class TablePost(models.Model):

    IS_BACKGROUND = True

    draft = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=None, null=True)
    title = models.CharField(max_length=63, default='')
    description = models.TextField(max_length=2047, default='')
    readme = models.TextField(max_length=2047, null=True)
    script_js = models.TextField(max_length=4095, null=True, blank=True)
    style_css = models.FileField(upload_to='styles_css/', null=True, blank=True)
    private_post = models.BooleanField(default=False)
    number_of_like = models.BigIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def add_like(self, like_from, **kwargs):
        like = not kwargs.pop('dislike', False)
        table_like = TableLike.objects.create(like_from=like_from, post=self, like=like)

        if like:
            self.number_of_like =+ 1
            self.save()

        return table_like

    def is_background(self):
        return self.IS_BACKGROUND

    def get_background_instructions(self):
        if self.is_background():
            return "<div id=\"background" + str(self.id) + "\" class=\"digital-art-background\">"
        else:
            return None


class TableLike(models.Model):

    like_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(TablePost, on_delete=models.CASCADE, related_name='table_like_set')
    date = models.DateTimeField(auto_now=True)
    like = models.BooleanField(default=True)

    class Meta:
        unique_together = [['like_from', 'post']]

    @staticmethod
    def check_liked(post, user):
        if TableLike.objects.filter(post=post, like_from=user, like=True).first():
            return True
        else:
            return False

    def edit_like(self, like):
        if like and not self.like:
            self.post.number_of_like =+ 1
        elif not like and self.like:
            self.post.number_of_like =- 1

        self.like = like
        self.post.save()
        self.save()

    def check_disliked(post, user):
        if TableLike.objects.filter(post=post, like_from=user, like=False).first():
            return True
        else:
            return False


class TableComment(models.Model):

    comment_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(TablePost, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1023)
    date = models.DateTimeField(auto_now_add=True)
