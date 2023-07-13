import requests
from django.shortcuts import render


def catdog_view(request):
    if request.method == "GET":
        return render(request, 'catdog.html')
    if request.method == "POST":
        if 'cat' in request.POST:
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            response_dict = response.json()
            url = response_dict[0]['url']
            content = {'url': url}
        elif 'dog' in request.POST:
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            response_dict = response.json()
            url = response_dict['message']
            content = {'url': url}
        else:
            raise AttributeError('smth wrong')
        return render(request, 'pet.html', context=content)
