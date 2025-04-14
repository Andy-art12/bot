from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='7 класс', callback_data='buy')
    kb_builder.button(text='8 класс', callback_data='more_foto')
    kb_builder.button(text='9 класс ️', callback_data='callback')
    kb_builder.button(text='10 класс ️', callback_data='next')
    kb_builder.button(text='11 класс ️', callback_data='next')

    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()
