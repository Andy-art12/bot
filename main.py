import asyncio

import logging #для логирования (отладки)

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties  #редактирование сообщений HTML
from aiogram.filters import Command

#хранение токенов
from dotenv import load_dotenv
import os

from core.keyboards.first_kb import first_kb

#Загрузка токена
load_dotenv()
token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

#Загрузка бота
async def start_bot(bot: Bot):

    await bot.send_message(admin_id, f'start bot')
# async def get_start(bot: Bot,m: Message):
    # await bot.send_message(m.from_user.id,f'{m.from_user.id}')

async def get_start(m: Message, bot: Bot):
    await bot.send_message(m.from_user.id, f'привет {m.from_user.id}', reply_markup=first_kb())

async def start():
    # logging.basicConfig(level=logging.INFO) #разкоментировать для отлпдки
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))

    #Обьявления диспатчера
    dp = Dispatcher()

    #===========DP REGISTERS======================
    dp.startup.register(start_bot)

    dp.message.register(get_start, Command(commands='start'))
    #==============================================


    #запуск и остановка бота
    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()

#Бесконечный цикл для бота
if __name__ == '__main__':
    asyncio.run(start())
