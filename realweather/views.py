import requests
from django.shortcuts import render

# Create your views here.


from .forms import CityForm
from .models import City


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial' \
          '&appid={Api Key}'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        # print(city_weather)
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'humidity': city_weather['main']['humidity'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, "home.html", context)
