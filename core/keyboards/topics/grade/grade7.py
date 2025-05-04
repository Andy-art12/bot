from aiogram.utils.keyboard import InlineKeyboardBuilder


def grade7_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='ФСУ', callback_data='fcu7')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()