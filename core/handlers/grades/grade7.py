from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.topics.grade.grade7 import grade7_inline_kb
from core.keyboards.basic_kb import go_back_kb

async def choise_topic_7(call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer('Выберите тему: ', reply_markup=grade7_inline_kb())

async def fcu7 (call: CallbackQuery, bot: Bot):
    await call.answer()
    await call.message.answer_photo("AgACAgIAAxkBAAIB8WgXU1SsjjEEzBVkL24KTmwoENTvAALn8TEbMj24SCUDq9yl5a9MAQADAgADeQADNgQ", reply_markup=go_back_kb())