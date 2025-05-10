from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from core.keyboards.topics.grade.grade10 import grade10_inline_kb
from core.keyboards.basic_kb import go_back_kb

async def choise_topic_10(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ', reply_markup=grade10_inline_kb())

async def fcu10(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer_photo("AgACAgIAAxkBAAICfmgfWfsShFxVaAoBKmP-M9Bg3BhAAAIz7zEbe64AAUno4W6lYKcMwwEAAwIAA3kAAzYE",reply_markup=go_back_kb())