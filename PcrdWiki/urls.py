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
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from pcrd_unpack.sitemaps import UnitSitemap, EquimpmentSitemap

sitemaps = {

    'unit': UnitSitemap,
    'equipment': EquimpmentSitemap,
}

urlpatterns = [
    path("", include("pcrd_unpack.urls")),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'pcrd_unpack.views.handler404'