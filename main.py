import asyncio


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('TOKEN')

async def start_bot(bot: Bot, m: Message):
    await bot.send_message(1034762341, f'start bot')
async def get_start(m: Message, bot: Bot):
    await bot.send_message(m.from_user.id, f'привет')
async def start():
    bot = Bot(token=token)

    dp = Dispatcher()

    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()

    dp.startup.register(start_bot)
    dp.message.register()










if __name__ == '__main__':
    asyncio.run(start())

