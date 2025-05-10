from aiogram.utils.keyboard import InlineKeyboardBuilder


def grade9_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='нач.мат.анал', callback_data='fcu9')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()