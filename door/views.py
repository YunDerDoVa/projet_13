from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import RegisterForm, SettingsForm, PrivacySettingsForm


# Create your views here.
def register(request):

    """ This view do it :
    - redirect to dashboard if user is authenticated.
    - register and login a new user for POST requests
    - render register template for GET requests """

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            if cd['password1'] == cd['password2']:
                user = User.register_new_user(cd['username'], cd['email'], cd['password1'])
                login(request, user)
                return redirect('discover')

    context = {
        'form': form,
    }

    return render(request, 'door/register.html.django', context)


@login_required(login_url='login')
def settings(request):
    """ This view show us our settings forms. If a form is edited, it add a
    toast to the toasts' list to give a feedback to the user. """

    form = SettingsForm(instance=request.user)
    privacy_form = PrivacySettingsForm(instance=request.user.privacy_settings)

    toasts = []

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=request.user)
        privacy_form = PrivacySettingsForm(request.POST, instance=request.user.privacy_settings)

        if form.is_valid():
            form.save()

        if privacy_form.is_valid():
            privacy_form.save()

        if form.has_changed():
            toasts.append('Global Settings Changed')

        if privacy_form.has_changed():
            toasts.append('Privacy Settings Changed')

    context = {
        'form': form,
        'privacy_form': privacy_form,
        'toasts': toasts,
    }

    return render(request, 'door/settings.html.django', context)
