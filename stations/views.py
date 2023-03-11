from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    file_bus_stations: list = []

    path = settings.BUS_STATION_CSV
    
    page_number = int(request.GET.get('page', 1))
    
    with open(path, newline='', encoding='utf-8') as csv_file:
        file_csv = csv.DictReader(csv_file)
        for stroka in file_csv:
            file_bus_stations.append(stroka)

    pagin_stat = Paginator(file_bus_stations, 10)
    page = pagin_stat.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
