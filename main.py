import asyncio
import requests


import logging #для логирования (отладки)

from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties  #редактирование сообщений HTML
from aiogram.filters import Command
import core.handlers.basic

#хранение токенов
from dotenv import load_dotenv
import os

from core.keyboards.basic_kb import first_kb

import core.handlers.grades.grade7
import core.handlers.grades.grade8
import core.handlers.grades.grade9
import core.handlers.grades.grade10
import core.handlers.grades.grade11
#Загрузка токена
load_dotenv()
token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')
url = f"https://api.telegram.org/bot{token}/deleteWebhook"
response = requests.get(url)
print(response.json())

#Загрузка бота
async def start_bot(bot: Bot):
    await bot.send_message(admin_id, f'start bot')



async def link(m: Message, bot: Bot):
    await bot.send_message(m.from_user.id, f'https://aliexpress.ru/', reply_markup=first_kb())
async def link_gdz(m: Message, bot: Bot):
    await bot.send_message(m.from_user.id, f'📚')
    await bot.send_message(m.from_user.id, f'https://gdz.ru/', reply_markup=first_kb())


async def start():
    # logging.basicConfig(level=logging.INFO) #разкоментировать для отлпдки
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))

    #Обьявления диспатчера
    dp = Dispatcher()

    #===========DP REGISTERS======================
    dp.startup.register(start_bot)

    dp.message.register(core.handlers.basic.get_start, Command(commands='start'))
    dp.message.register(core.handlers.basic.get_start, F.text == 'главная 🏠')
    dp.message.register(core.handlers.basic.get_help, Command(commands='help'))

    dp.callback_query.register(core.handlers.grades.grade7.choise_topic_7, F.data.startswith('7grade'))
    dp.callback_query.register(core.handlers.grades.grade8.choise_topic_8, F.data.startswith('8grade'))
    dp.callback_query.register(core.handlers.grades.grade9.choise_topic_9, F.data.startswith('9grade'))
    dp.callback_query.register(core.handlers.grades.grade10.choise_topic_10, F.data.startswith('10grade'))
    dp.callback_query.register(core.handlers.grades.grade11.choise_topic_11, F.data.startswith('11grade'))

    dp.callback_query.register(core.handlers.grades.grade7.fcu7, F.data.startswith('fcu7'))
    dp.callback_query.register(core.handlers.grades.grade8.fcu8, F.data.startswith('fcu8'))
    #dp.callback_query.register(core.handlers.grades.grade9.fcu9, F.data.startswith('fcu9'))
    #dp.callback_query.register(core.handlers.grades.grade10.fcu10, F.data.startswith('fcu10'))
    #dp.callback_query.register(core.handlers.grades.grade11.fcu11, F.data.startswith('fcu11'))

    @dp.message(lambda m: m.photo)
    async def handle_photo(message: types.Message):
        # Берём file_id фото в наилучшем качестве (последний элемент массива)
        file_id = message.photo[-1].file_id

        await message.reply(
            f"🖼 File ID этого фото:\n"
            f"<code>{file_id}</code>\n\n"
            f"Размер: {message.photo[-1].file_size // 1024} KB",
            parse_mode="HTML"
    )

    #==============================================


    #запуск и остановка бота
    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()

#Бесконечный цикл для бота
if __name__ == '__main__':
    asyncio.run(start())
