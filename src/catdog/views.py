import datetime

import requests
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from catdog.forms import PetFilterForm
from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS, EMAIL_HOST_USER
from logging import getLogger
logger = getLogger()

def catdog_view(request):
    if request.method == "GET":
        data = {'form': PetFilterForm()}
        return render(request, 'catdog.html', data)
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
                                   species=data_for_write['species'],
                                   type=data_for_write['type'])
        data = {'url': data_for_write['url']}
        return render(request, 'petsaved.html', context=data)


def send_email(request):
    url = request.POST.get('url')
    send_mail(
        "Subject here",
        f"Here is the link to image - {url}",
        EMAIL_HOST_USER,
        [EMAIL_HOST_USER],
        fail_silently=False
    )
    return render(request, 'success_send_mail.html', {'url': url})


def pet_filter(request):
    if request.method == 'POST':
        form = PetFilterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pets = AnimalImage.objects.filter(Q(species=data.get('pet')) &
                                              Q(type=data.get('type_img')))
            logger.info(f'{pets}')
            return render(request, 'pet_filter.html', {'pets': pets})
