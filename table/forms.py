from django import forms

from .models import TablePost


class PostForm(forms.ModelForm):
    """ This form is a ModelForm with TablePost as model.
    He is displayed in the table_publish and table_edit view. """

    class Meta:
        model = TablePost
        exclude = [
            'draft',
            'user',
            'number_of_like',
            'creation_date',
            'last_update_date',
        ]
