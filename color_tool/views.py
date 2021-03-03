from django.shortcuts import render, redirect

import requests


# Create your views here.
def screen(request):
    """ This view show a colored screen with differents color values """

    if 'hexa' in request.GET.keys():
        hexa = request.GET.get('hexa')
        url = "https://www.thecolorapi.com/id?hex={}".format(hexa)
    elif 'rgb' in request.GET.keys():
        rgb = request.GET.get('rgb')
        url = "https://www.thecolorapi.com/id?rgb={}".format(rgb)
    elif 'hsl' in request.GET.keys():
        hsl = request.GET.get('hsl')
        url = "https://www.thecolorapi.com/id?hsl={}".format(hsl)
    else:
        return redirect('index')

    r = requests.get(url)
    data = r.json()

    text_color = request.GET.get(
        'text', data.get(
            'contrast', {
                'value': 'white'})['value'])
    text_background_color = request.GET.get('text_background_color', 'none')

    context = {
        'data': data,
        'text_color': text_color,
        'text_background_color': text_background_color,
    }

    return render(request, 'color_tool/screen.html.django', context)
