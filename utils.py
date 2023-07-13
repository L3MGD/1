import datetime

import requests

API_KEY = "9df35aca72b4db0fb6ae953bc4dd8ac8"


def get_weather_data(city):
    try:
        geo_api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        response = requests.get(geo_api_url)
        cities = response.json()
        lat, lon = cities[0]["lat"], cities[0]["lon"]

        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        response = requests.get(weather_api_url)
        data = response.json()
        timestamp = data["dt"]
        date = datetime.datetime.fromtimestamp(timestamp)
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"]
        weather_data = {
            "date": date,
            "weather": weather,
            "temp": temp,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction
        }

        return weather_data
    except Exception as e:
        print("Ошибка при получении данных о погоде:", e)


def get_cat_url():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    if data and 'url' in data[0]:
        photo_url = data[0]['url']
        return photo_url


def get_dog_url():
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    data = response.json()
    if data and 'url' in data[0]:
        photo_url = data[0]['url']
        return photo_url
