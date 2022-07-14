from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
import aiofiles
from telegrambot.little_big_bot.config import number, count_of_attemps



bot = Bot('5412674596:AAEn0fN0AvcyHgNhpHuH69-RnSL3IzZRIE8')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    if count_of_attemps == 1:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name},я загадал число,'
                                                     f'попробуй его угадать')
    else:
        await bot.send_message(message.from_user.id, 'Введите число')


@dp.message_handler()
async def info(message: types.Message):
    global number, count_of_attemps

    try:
        if int(message.text) == number:
            await  message.answer(f'Поздравляю. Вы угадали!\nКоличество попыток: {count_of_attemps}')
            count_of_attemps = 1

        elif int(message.text) < number:
            await  message.answer(f'Ваше число меньше загаданного')
            count_of_attemps += 1


        else:
            await message.answer(f'Ваше число больше загаданного')
            count_of_attemps += 1


    except:
        await  bot.send_message(message.from_user.id,
                                f'пиши целое число')


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)
