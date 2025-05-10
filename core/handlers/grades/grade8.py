from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.topics.grade.grade8 import grade8_inline_kb
from core.keyboards.basic_kb import go_back_kb

async def choise_topic_8(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ', reply_markup=grade8_inline_kb())

async def fcu8(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer_photo("AgACAgIAAxkBAAICM2gaRixQ6voYsjLfWz1BcwdWme1PAAIi6DEbgkDZSFjpiI6avDOfAQADAgADeQADNgQ",reply_markup=go_back_kb())