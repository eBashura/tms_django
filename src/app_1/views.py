import csv
import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from app_1.forms import UserForm


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
    if not os.path.exists('users.csv'):
        with open('users.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'lastname', 'age'])
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        with open('users.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, lastname, age])
        return HttpResponse(f'name - {name}, lastname - {lastname}, age - {age}')
    else:
        template = loader.get_template('form.html')
        response = template.render({}, request)
        return HttpResponse(response)


def add_user_v2(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            name = data.get('name')
            lastname = data.get('lastname')
            age = data.get('age')
            # content = {'fn': name,
            #            'ln': lastname,
            #            'age': age
            #            }
            content = {'user': {'fn': name, 'ln': lastname, 'age': age}}
            return render(request, 'django_06_display.html', content)
        else:
            errors = form.errors
            return HttpResponse(f'error - {errors}')
    else:
        return render(request, 'django_06_form.html', {'form': UserForm()})
