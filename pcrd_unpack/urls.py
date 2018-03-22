"""PcrdWiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import django.contrib.auth.views
from datetime import datetime
import pcrd_unpack.forms
from . import views


app_name = 'pcrd_unpack'

urlpatterns = [
    path("", views.QuestAreaListView.as_view(), name="index"),
    path("area/<int:area_id>", views.QuestAreaDetailView.as_view(), name="area_detail"),
    path("equipment", views.EqupimentView.as_view(), name="equipment"),
    path('login/',
         django.contrib.auth.views.login,
         {
             'template_name': 'app/login.html',
             'authentication_form': pcrd_unpack.forms.BootstrapAuthenticationForm,
             'extra_context':
                 {
                     'title': 'Log in',
                     'year': datetime.now().year,
                 }
         },
         name='login'),
    path('logout',
         django.contrib.auth.views.logout,
         {
             'next_page': '/',
         },
         name='logout'),
]
