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
    path("", views.IndexView.as_view(), name="index"),
    path("unit_data/<int:unit_id>", views.UnitJsonView.as_view(), name="unit_json"),
    path("unit/<int:unit_id>", views.UnitDetailView.as_view(), name="unit"),
    path("unit/", views.UnitListView.as_view(), name="unit_list"),
    path("summary/", views.UnitSummaryView.as_view(), name="unit_summary"),
    path("item/<int:item_id>", views.ItemView.as_view(), name="item"),
    path("equipment_list/", views.EquipmentListView.as_view(), name="equipment_list"),
    path("area/", views.QuestAreaListView.as_view(), name="area"),
    path("area/<int:area_id>", views.QuestAreaDetailView.as_view(), name="area_detail"),
    path("equipment/<int:equipment_id>", views.EquipmentView.as_view(), name="equipment"),
    path('login/',
         django.contrib.auth.views.login,
         {
             'template_name': 'pcrd_unpack/login.html',
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
