from aiogram.utils.keyboard import InlineKeyboardBuilder


def grade8_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='форм.сокр.умн', callback_data='fcu8')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()