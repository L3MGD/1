import requests
from aiogram import Bot, Dispatcher, types

TOKEN = "6372341859:AAGFRW_Qypw3Qvwq6aoA1kaNuWQhm0tZuvI"

API_KEY = "9df35aca72b4db0fb6ae953bc4dd8ac8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот погоды. Введите название города, чтобы получить погоду.")


@dp.message_handler()
async def get_weather(message: types.Message):
    city = message.text
    weather_data = get_weather_data(city)
    if weather_data:
        await message.reply(weather_data)
    else:
        await message.reply("Не удалось получить данные о погоде. Пожалуйста, попробуйте еще раз.")


def get_weather_data(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather = data["weather"][0]["main"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            return f"Погода в {city}: {weather}\nТемпература: {temp}°C\nВлажность: {humidity}%"
    except Exception as e:
        print("Ошибка при получении данных о погоде:", e)
    return None


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dispatcher=dp, skip_updates=True)