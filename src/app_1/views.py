import datetime

from django.http import HttpResponse
from django.shortcuts import render


def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)
