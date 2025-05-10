from aiogram.utils.keyboard import InlineKeyboardBuilder


def grade11_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='тригонометрия', callback_data='fcu11')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()