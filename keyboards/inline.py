from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


def create_main_menu_kb(*buttons_keys: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_RU['buttons'][button]
        if button in LEXICON_RU['buttons'] else button,
        callback_data=button) for button in buttons_keys],
        width=1)
    return kb_builder.as_markup()
