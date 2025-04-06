from aiogram.utils.keyboard import ReplyKeyboardBuilder

def first_kb():
    kb_build = ReplyKeyboardBuilder()
    kb_build.button(text='/start')
    kb_build.button(text='помощь')
    kb_build.button(text='решить')
    kb_build.button(text='/каталог')
    kb_build.button(text='гдз📚')
    kb_build.button(text='/каталог')

    kb_build.adjust(2, 2)
    return kb_build.as_markup(resize_keyboard=True)
