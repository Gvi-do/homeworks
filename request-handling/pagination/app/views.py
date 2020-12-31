import csv
import urllib

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

def generator_bus_station(file):
    for row in file:
        bus = {}
        bus['Name'] = row['Name']
        bus['Street'] = row['Street']
        bus['District'] = row['District']
        yield bus
content = []


with open('data-398-2018-08-30.csv', encoding='cp1251', newline='') as csvf:
    reader = csv.DictReader(csvf)
    for i in generator_bus_station(reader):
        content.append(i)

def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(content, settings.ITEM_PER_PAGE)
    page_obj = paginator.get_page(current_page)
    next_page_namber = {}
    if page_obj.has_next():
        next_page_namber['page'] = page_obj.next_page_number()
        next_page_url = f"{reverse('bus_stations')}?{urllib.parse.urlencode(next_page_namber)}"
    else:
        next_page_url = None

    prev_page_number = {}
    if page_obj.has_previous():
        prev_page_number['page'] = page_obj.previous_page_number()
        prev_page_url = f"{reverse('bus_stations')}?{urllib.parse.urlencode(prev_page_number)}"
    else:
        prev_page_url = None

    return render(request, 'index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

