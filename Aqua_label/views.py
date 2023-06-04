from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from API.models import *
from django import forms


class UserForm(forms.Form):
    name = forms.CharField()


def functions(request):
    cursor = connection.cursor()
    submitbutton = request.POST.get("submit")

    value = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        value = form.cleaned_data.get("name")
    if submitbutton == 'AllAuditions':
        cursor.execute('select AllAuditions (%s)', (value,))
    elif submitbutton == 'Welcome':
        cursor.execute('select welcome (%s)', (value,))
    else:
        cursor.execute('select MostListenedTo (%s)', (value,))
    submitbutton = 'Submit'
    results = cursor.fetchall()
    return render(request, "functions.html",
                  {"form": form, 'results': results, 'name': value, 'submitbutton': submitbutton})


def allSales(request):
    cursor = connection.cursor()
    cursor.execute('call AllSales')
    results = cursor.fetchall()
    return render(request, "functions.html", {'results': results})


def auditionsOfAlbum(request):
    cursor = connection.cursor()
    cursor.execute('call AuditionsOfAlbum')
    results = cursor.fetchall()
    return render(request, "functions.html", {'results': results})


def getNamesArtists(request):
    cursor = connection.cursor()
    cursor.execute('call GetNamesArtists')
    results = cursor.fetchall()
    return render(request, "functions.html", {'results': results})


def get_menu_context(request):
    menu = [
        dict(title='Главная', url=reverse('index')),
    ]
    return menu


def function_page(request):
    return render(request, 'functions.html')


def index_page(request):
    context = {'menu': get_menu_context(request), 'author': 'Lunatic',
               'creation_date': '10.12.2022', 'pages_count': 1,
               'user': request.user, 'pagename': 'Aqua_label'}
    response = Artist.objects.all()
    context['Items'] = response
    return render(request, 'base.html', context)


def events_page(request):
    context = {'menu': get_menu_context(request), 'author': 'Lunatic',
               'creation_date': '10.12.2022', 'pages_count': 1,
               'user': request.user, 'pagename': 'Aqua_label'}
    response = Event.objects.all()
    context['Items'] = response
    return render(request, 'events.html', context)


def venue_page(request, inp_venue):
    context = {'menu': get_menu_context(request), 'author': 'Lunatic',
               'creation_date': '10.12.2022', 'pages_count': 1,
               'user': request.user, 'pagename': 'Aqua_label'}
    response = Event.objects.select_related().filter(venue=inp_venue)
    context['Items'] = response
    return render(request, 'events.html', context)


def artist_page(request, inp_id):
    context = {'menu': get_menu_context(request), 'author': 'Lunatic',
               'creation_date': '10.12.2022', 'pages_count': 1,
               'user': request.user, 'pagename': 'Aqua_label'}
    response = Artist.objects.get(pk=inp_id)
    context['item'] = response
    response = Event.objects.select_related().filter(id_artist=response.id_artist)
    context['Items'] = response[:8]
    return render(request, 'events.html', context)
