from aiogram.utils.keyboard import ReplyKeyboardBuilder

def first_kb():
    kb_build = ReplyKeyboardBuilder()
    kb_build.button(text='/start')
    kb_build.button(text='/help')
    kb_build.button(text='/solve')

    kb_build.adjust(2, 1)
    return kb_build.as_markup(resize_keyboard=True)
