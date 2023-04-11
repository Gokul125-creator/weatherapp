
import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    city = 'London'
    if 'city' in request.GET:
        city = request.GET['city']
    r = requests.get(url.format(city, '2868a7bb0e95fdae4db5fa3eed66e974')).json()
    weather_data = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    return render(request, 'index.html', {'weather_data': weather_data})
