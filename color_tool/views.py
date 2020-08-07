from django.shortcuts import render


# Create your views here.
def screen(request):

    hexa_color = request.GET.get('hexa', 'green')
    text_color = request.GET.get('text', 'white')
    text_background_color = request.GET.get('text_background_color', 'rgba(0, 0, 0, 0.21)')
    context = {
        'hexa_color': hexa_color,
        'text_color': text_color,
        'text_background_color': text_background_color,
    }

    return render(request, 'color_tool/screen.html.django', context)
