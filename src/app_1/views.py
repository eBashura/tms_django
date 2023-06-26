import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)


def two_pow(request, number):
    result = 2 ** int(number)
    return HttpResponse(f'2 ** {number} = {result}')


def hello_admin(request):
    return HttpResponse('Hello, admin!')


def hello_guest(request, name):
    return HttpResponse(f'Hello, {name}!')


def hello_user(request, user):
    if user == 'admin':
        return redirect('hello_admin')
    else:
        return redirect('hello_guest', guest=user)


def my_word(request, word):
    if len(word) % 2:
        return redirect('get_time')
    else:
        return HttpResponse(f'{word[::2]}')


def login(request):
    if request.method == 'POST':
        pass
    else:
        name_2 = request.GET.get('name')
        return redirect('success', name=name_2)


def success(request, name):
    return HttpResponse(f'Welcome, {name}')


def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        return HttpResponse(f'name - {name}, lastname - {lastname}, age - {age}')
    else:
        pass
