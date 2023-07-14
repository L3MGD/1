import random

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from utils import get_weather_data, get_cat_url, get_dog_url

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Привет! Я бот погоды. Введите название города, чтобы получить погоду. можете написать секретную команду"
        " /sendmusic она прикольная и отправит вам музыку или я могу отправить котика /cat или собаку /dog")


async def send_video(chat_id: int, path: str):
    video = types.InputFile(path)
    await bot.send_video(chat_id=chat_id, video=video)


@dp.message_handler(commands=['sendvideo'])
async def _(message: types.Message):
    chat_id = message.chat.id
    await send_video(chat_id, 'phonk.mp4')


@dp.message_handler(commands=['sendmusic'])
async def send_music(message: types.Message):
    x = random.choice([1, 2, 3])
    chat_id = message.chat.id

    if x == 1:
        await send_video(chat_id, "video.mp4")
    elif x == 2:
        await send_video(chat_id, "video (1).mp4")
    elif x == 3:
        await send_video(chat_id, "video (2).mp4")


  
@dp.message_handler()
async def get_weather(message: types.Message):
    city = message.text
    day_weather = get_weather_data(city)

    if day_weather:
        weather = day_weather["weather"]
        temp = day_weather["temp"]
        humidity = day_weather["humidity"]
        wind_speed = day_weather["wind_speed"]
        wind_direction = day_weather["wind_direction"]
        text = f"Погода в {city}: {weather}\nТемпература: {temp}°C\nВлажность: {humidity}%\nСила ветра: {wind_speed} м/с, направление ветра: {wind_direction}°"
        await message.reply(text)
    else:
        await message.reply("Не удалось получить данные о погоде. Пожалуйста, попробуйте еще раз.")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dispatcher=dp, skip_updates=True)
