"""Aqua_label URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *


urlpatterns = [
    path('', index_page, name='index'),
    path('events/', events_page, name='events_page'),
    path('events/venue/<str:inp_venue>', venue_page, name='venue_page'),
    path('events/artists/<int:inp_id>', artist_page, name='artist_page'),
    path('functions/', functions, name='functions'),
    path('functions/allSales/', allSales, name='allSales'),
    path('functions/auditionsOfAlbum/', auditionsOfAlbum, name='auditionsOfAlbum'),
    path('functions/getNamesArtists/', getNamesArtists, name='getNamesArtists'),
    path('admin/', admin.site.urls),
    path('api/', include('API.urls'))
]
