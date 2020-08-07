from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import User
from .forms import RegisterForm


# Create your views here.
def register(request):

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