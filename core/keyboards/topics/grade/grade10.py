from aiogram.utils.keyboard import InlineKeyboardBuilder


def grade10_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='повторение за пред.классы', callback_data='fcu10')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()