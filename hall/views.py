from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'hall/index.html.django')


def discover(request):
    return render(request, 'hall/discover.html.django')
