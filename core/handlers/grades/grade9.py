from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from core.keyboards.topics.grade.grade9 import grade9_inline_kb
from core.keyboards.basic_kb import go_back_kb

async def choise_topic_9(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ', reply_markup=grade9_inline_kb())

async def fcu9(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer_photo("AgACAgIAAxkBAAICRGgfUa8SM1SVA2y0vdyd6jZQxbOiAAL27jEbe64AAUkiJKC7x8yObQEAAwIAA3kAAzYE",reply_markup=go_back_kb())