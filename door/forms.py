from django import forms
from .models import User, Privacy


class RegisterForm(forms.Form):
    """ A register form with all fields we need to create a new user. """

    username = forms.CharField(
        label='Username',
        max_length=127)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        max_length=127)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(),
        max_length=127)


class SettingsForm(forms.ModelForm):
    """ This form is necessary to update Users' Profile. """

    class Meta:
        model = User
        fields = ['avatar', 'banner']


class PrivacySettingsForm(forms.ModelForm):
    """ This form is necessary to update privacy settings. """

    class Meta:
        model = Privacy
        exclude = ['user', 'disable_account']
