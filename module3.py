from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
import pyautogui
import re
import random
from time import sleep
import time


import yt_download as yt
import config 


def random_id():
    return random.randint(0, 1000000)

bot = Bot(config.TOKEN)
URL = "https://painmo.herokuapp.com/"
dp = Dispatcher(bot)


   
@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    await message.reply(config.STARTEXT)
    await message.delete()

   
'''
@dp.message_handler(commands=['screenhot'])
async def process_help_command(message: types.Message):
    im1 = pyautogui.screenshot('screenshot.png')
    await message.reply_document(open('screenshot.png', 'rb'))
    time.sleep(600)
    im2 = pyautogui.screenshot('screenshot1.png')
    await message.reply_document(open('screenshot1.png', 'rb'))
    time.sleep(600)
    im3 = pyautogui.screenshot('screenshot3.png')
    await message.reply_document(open('screenshot3.png3', 'rb'))
    time.sleep(600)
    im3 = pyautogui.screenshot('screenshot4.png')
    await message.reply_document(open('screenshot4.png', 'rb'))
    time.sleep(600)

'''



@dp.message_handler(commands=['screen'])
async def process_help_command(message: types.Message):
    im4 = pyautogui.screenshot('my_screenshot.png')
    await message.reply("Відправляю..")
    await message.reply_document(open('my_screenshot.png', 'rb'))
    



print("Оно живое !")
executor.start_polling(dp)