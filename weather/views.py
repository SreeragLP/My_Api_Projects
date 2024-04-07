from django.shortcuts import render
import requests
from datetime import datetime,timedelta
import pytz

def select_city(request):
    return render(request, 'select_city.html')


def view_weather(request):
    selected_city = request.GET.get('selected_city', 'London')  # Default to 'London' if no city selected
    api_key = '58a55092c77d8dd28afe3a936fe57e9e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={selected_city}&appid={api_key}'

    response = requests.get(url)
    weather_data = response.json()

    # Temperature in Kelvin
    temperature_kelvin = weather_data['main']['temp']
    # Convert Kelvin to Celsius, round to the nearest whole number, and convert to an integer
    temperature_celsius = int(round(temperature_kelvin - 273.15))

    weather_description = weather_data['weather'][0]['description']

    # Additional weather details
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    wind_direction = weather_data['wind']['deg']
    pressure = weather_data['main']['pressure']
    visibility = weather_data['visibility']
    sunrise_timestamp = weather_data['sys']['sunrise']
    sunset_timestamp = weather_data['sys']['sunset']
    timezone_offset = weather_data['timezone']  # Timezone offset in seconds


    sunrise_utc = datetime.utcfromtimestamp(sunrise_timestamp)  # Convert sunrise timestamp to UTC datetime
    sunset_utc = datetime.utcfromtimestamp(sunset_timestamp)  # Convert sunset timestamp to UTC datetime

    # Apply timezone offset to sunrise and sunset times
    sunrise_local = sunrise_utc + timedelta(seconds=timezone_offset)
    sunset_local = sunset_utc + timedelta(seconds=timezone_offset)

    # Format sunrise and sunset times as strings in 12-hour clock format with AM/PM
    sunrise_time = sunrise_local.strftime('%I:%M %p')
    sunset_time = sunset_local.strftime('%I:%M %p')

    context = {
        'selected_city': selected_city,
        'temperature': temperature_celsius,
        'weather_description': weather_description,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'wind_direction': wind_direction,
        'pressure': pressure,
        'visibility': visibility,
        'sunrise_time': sunrise_time,
        'sunset_time': sunset_time,
    }

    return render(request, 'weather.html', context)
