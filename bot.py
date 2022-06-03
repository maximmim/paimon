￼from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize

import re
import os

from time import sleep


import yt_download as yt
import config 


bot = Bot(config.TOKEN)
URL = "https://painmo.herokuapp.com/"
dp = Dispatcher(bot)

b1 = KeyboardButton('Помощь')
b2 = KeyboardButton('Скачять')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2)

@dp.message_handler(commands=['s'])
async def process_help_command(message: types.Message):
    await message.reply("Вибири мову /rus , /ukr")

@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    await message.reply("Привіт!\n Я Паймон і допоможу завантажити відео з будь-якого сайту якщо потрібна допомога пиши /help")
@dp.message_handler(commands=['rus'])
async def process_help_command(message: types.Message):
    await message.reply("Такої мови немає")

@dp.message_handler(commands=['ukr'])
async def process_help_command(message: types.Message):
    await message.reply("Ось мова готово")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Надішліть мені посилання на відео \n і я допоможу завантажити його")
@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):
    if message.text == 'Допомога':
            await message.reply("Надішліть мені посилання на відео \n і я допоможу завантажити його")

    try:
        
        echo_download=yt.Downloader(message.text)
        await message.reply("Побачила, починаю закачку...")
        videonote = open(echo_download.download_video(), 'rb')
    except:
        await message.reply("На жаль, сталася помилка... Перевірте правильність посилання")
        print('Error :(')
        return
    await message.reply("Готово, видео зкачено на сервер.\nВідправляю...",)
    try:
        await bot.send_document(message.from_user.id, videonote)
    except:
        await bot.send_message(message.from_user.id, "На жаль, сталася помилка...")
    finally:
        videonote.close()








print("Оно живое !")
executor.start_polling(dp)