from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize

import re
import os 

from time import sleep

from numpy import number


import yt_download as yt
import config 
import time 
import random

'''***********************************************Фунции***************************************************************'''

def random_id():
    return random.randint(0, 1000000)
def random_dw ():
    return random.choice(y)
'''***********************************************Конвази*************************************************************'''





bot = Bot(token="2056524233:AAHQcvf4M7Y6vSzpVolJgyCkb0dUfQ5kvow")
dp = Dispatcher(bot)



'''**************************************Админская часть****************************************************'''








'''*****************************Клиенская часть***************************************'''





@dp.message_handler(commands=['start'])
async def commands_start(message: types.message):
    bot.send_message(config.STARTEXT)


@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):

       
       try:
           echo_download=yt.Downloader(message.text)
           await message.reply("Побачила, починаю закачку...")
           videonote = open(echo_download.download_video(), 'rb')
       except:
           await message.reply("На жаль, сталася помилка... Перевірте правильність посилання")
           print('Error :(')
           return
           
       try:
           await message.reply("Готово, видео зкачено на сервер.\nВідправляю...",)
           await bot.send_document(message.from_user.id, videonote)
       except:
           await bot.send_message(message.from_user.id, "На жаль, сталася помилка...")
       finally:
           videonote.close()


  




print("Оно живое !!!")
executor.start_polling(dp, skip_updates=True)