from django import forms


class RegisterForm(forms.Form):

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
