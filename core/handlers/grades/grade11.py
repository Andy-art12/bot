from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from core.keyboards.topics.grade.grade11 import grade11_inline_kb
from core.keyboards.basic_kb import go_back_kb

async def choise_topic_11(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ', reply_markup=grade11_inline_kb())

async def fcu11(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer_photo("AgACAgIAAxkBAAICjWgfW4Y5lJmfOSTmiP-ZGGQ0YdtFAAJx8jEbscP4SEaebsqGOeGkAQADAgADeQADNgQ",reply_markup=go_back_kb())