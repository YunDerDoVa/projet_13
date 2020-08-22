from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'library/home.html.django')

def legacy(request):
    return render(request, 'library/legacy.html.django')
