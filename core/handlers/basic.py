from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from core.keyboards.basic_kb import go_back_kb

async def get_start(m: Message, bot: Bot):
    # await bot.send_message(m.from_user.id, f'привет {m.from_user.id}', reply_markup=first_kb())
    await bot.send_message(m.from_user.id, f'Выберерите класс ')

async def get_help(m: Message, bot: Bot):
    await bot.send_message(m.from_user.id, f'Добрый день. \n\n'
                                           f'Данный бот может выдавать формулы по темам математики для разных клссов. 🏫\n\n'
                                           f'Выберете класс. Тему. И бот заботливо предоставит формулы для урока. 📚\n', reply_markup=go_back_kb())