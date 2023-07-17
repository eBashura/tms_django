"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app1.views import get_data, two_pow, hello_admin, hello_guest, hello_user, my_word, success, login, add_user
from catdog.views import catdog_view, save_catdog, send_email

urlpatterns = [
    path('', catdog_view,
         name='catdog'),
    path('save_catdog', save_catdog,
         name='save_catdog'),
    path('send_email', send_email,
         name='send_email')
]
