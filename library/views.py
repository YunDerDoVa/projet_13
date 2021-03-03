from django.shortcuts import render


# Create your views here.
def home(request):
    """ The library home view is where all documentations are writen. """

    return render(request, 'library/home.html.django')


def legacy(request):
    """ The legacy view displays legacy mentions. """

    return render(request, 'library/legacy.html.django')
