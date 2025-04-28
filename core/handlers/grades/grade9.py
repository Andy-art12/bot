from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

async def choise_topic_9(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ')