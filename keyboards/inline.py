from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_BUTTONS


def create_main_menu_kb(*buttons_keys: str) -> InlineKeyboardMarkup:
    # создаём билдер клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # добавляем строки с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_BUTTONS[button]
        if button in LEXICON_BUTTONS else button,
        callback_data=button) for button in buttons_keys],
        width=1)
    # возвращаем объект клавиатуры с кнопками
    return kb_builder.as_markup()
