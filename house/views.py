from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html.django')


def my_library(request):
    return render(request, 'my_library.html.django')


def my_likes(request):
    return render(request, 'my_likes.html.django')