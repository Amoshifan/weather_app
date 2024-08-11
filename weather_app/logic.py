# logic.py
import requests

API_KEY = "1297c548bd5fb6de8d35ee4f192ffce1"  # OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'].capitalize()
        }
        return weather_data
    else:
        raise Exception("City not found or API request failed.")
