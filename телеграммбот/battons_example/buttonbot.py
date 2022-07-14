from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils import executor
import logging
import os
import datetime


logging.basicConfig(level=logging.DEBUG, filename='mylog.log',
                    format='%(asctime)s | %(levelname)s | %(funcName)s: %(lineno)d | %(message)s',
                    datefmt='%H:%M:%S')
bot = Bot('5412674596:AAEn0fN0AvcyHgNhpHuH69-RnSL3IzZRIE8')
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}, я бот который отправит '
                                                 f'тебе твое же сообщение', reply_markup=user_kb)
    await bot.send_message(message.from_user.id, 'Можешь узнать дату', reply_markup=user_inline_kb)


@dp.message_handler(text='Пожелание доброго утра')
async def good_morning(message: types.Message):
    await bot.send_message(message.from_user.id, 'Доброе утро')


@dp.message_handler(text='Пожелание доброй ночи')
async def good_night(message: types.Message):
    await bot.send_message(message.from_user.id, 'Сmessage: types.Message):покойной ночи')


@dp.callback_query_handler(text='button_data')
async def reply_mes(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, 'Кнопка сработала')

    now_date = datetime.datetime.now()

    await bot.send_message(callback_query.from_user.id, f'{now_date.strftime("%d,%m,%y,%H:%M:%S")}')
    
   
@dp.message_handler(text = 'Узнать время')
async def time(message: types.Message):
    now_date = datetime.datetime.now()
    await bot.send_message(message.from_user.id, f'{now_date.strftime("%d,%m,%y,%H:%M:%S")}')
    
    
@dp.message_handler(text = 'Пожелание хорошего дня!')
async def day(message: types.Message):
	await bot.send_message(message.from_user.id, 'Хорошего дня!')

   
 
@dp.message_handler()
async def reply_message(message: types.Message):
    await message.reply(message.text)
    
    
button_good_morning = KeyboardButton('Пожелание доброго утра')
button_good_night = KeyboardButton('Пожелание доброй ночи')
button_goog_day = KeyboardButton('Пожелание хорошего дня!')
time = KeyboardButton('Узнать время')


user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_good_morning, button_good_night, time, button_goog_day)


button_date = InlineKeyboardButton(text = 'Время и дата', callback_data='button_data')
user_inline_kb = InlineKeyboardMarkup (resize_keyboard = True).row (button_date)


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)
