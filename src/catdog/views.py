import datetime

import requests
from django.core.mail import send_mail
from django.shortcuts import render

from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS


def catdog_view(request):
    if request.method == "GET":
        return render(request, 'catdog.html')
    if request.method == "POST":
        request.session.set_expiry(30)
        if 'cat' in request.POST:
            response = requests.get(URL_FOR_CATS)
            response_dict = response.json()
            url = response_dict[0]['url']
            content = {'url': url}
            type_img = url.split('.')[-1]
            data_for_session = {'url': url,
                                'species': AnimalImage.CHOICES_SP[0][0],
                                'type': type_img}
            request.session['data_for_session'] = data_for_session
        elif 'dog' in request.POST:
            response = requests.get(URL_FOR_DOGS)
            response_dict = response.json()
            url = response_dict['message']
            content = {'url': url}
            type_img = url.split('.')[-1]
            data_for_session = {'url': url,
                                'species': AnimalImage.CHOICES_SP[1][0],
                                'type': type_img}
            request.session['data_for_session'] = data_for_session
        else:
            raise AttributeError('smth wrong')
        return render(request, 'pet.html', context=content)


def save_catdog(request):
    if request.method == "POST":
        data_for_write = request.session['data_for_session']
        AnimalImage.objects.create(url=data_for_write['url'],
                                   species=['species'],
                                   type=data_for_write['type'])
        content = {'url': data_for_write['url']}
        return render(request, 'petsaved.html', context=content)


def send_email(request):
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["eBashura@gmail.com"],
        fail_silently=False
    )
