from services.MessageButton import get_all_message_btns
from models import MessageButton

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from lexicon.lexicon import LEXICON_BUTTONS


# def create_main_menu_kb(*buttons_keys: str) -> InlineKeyboardMarkup:
#     # создаём билдер клавиатуры
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     # добавляем строки с кнопками
#     kb_builder.row(*[InlineKeyboardButton(
#         text=LEXICON_BUTTONS[button]
#         if button in LEXICON_BUTTONS else button,
#         callback_data=button) for button in buttons_keys],
#         width=1)
#     # возвращаем объект клавиатуры с кнопками
#     return kb_builder.as_markup()


def is_btn_type_url(button_type: str) -> bool:
    return button_type == 'btn-url'


def is_btn_type_message(button_type: str) -> bool:
    return button_type == 'btn-message'


def create_url_btn(btn_text: str, btn_url: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=btn_text, url=btn_url)


def create_meassage_btn(btn_text: str, callback_name: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=btn_text, callback_data=callback_name)


def create_inline_button(button_data: str, button_type: str, button_func: str) -> InlineKeyboardButton:
    if is_btn_type_url(button_type):
        inline_btn: InlineKeyboardButton = create_url_btn(button_data, button_func)
    elif is_btn_type_message(button_type):
        inline_btn: InlineKeyboardButton = create_meassage_btn(button_data, button_func)
    return inline_btn


def generate_keyboard(mesage_id: int) -> InlineKeyboardMarkup:
    buttons: list[MessageButton] = get_all_message_btns(mesage_id)

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    inline_buttons: list[InlineKeyboardButton] = []

    for button in buttons:
        button_data: str = button.data
        button_type: str = button.type
        button_func: str = button.function_data

        inline_button: InlineKeyboardButton = create_inline_button(button_data, button_type, button_func)
        inline_buttons.push(inline_button)

    keyboard_builder.row(inline_buttons, width=1)

    return keyboard_builder.as_markup()
