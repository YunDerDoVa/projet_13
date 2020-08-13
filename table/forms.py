from django import forms

from .models import TablePost


class PostForm(forms.ModelForm):

    class Meta:
        model = TablePost
        exclude = [
            'draft',
            'user',
            'number_of_like',
            'creation_date',
            'last_update_date',
        ]
