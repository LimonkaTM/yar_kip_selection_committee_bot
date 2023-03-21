from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from services.MessageButton import get_msg_btns


async def create_msg_menu(msg_id: str) -> InlineKeyboardMarkup:
    '''
    Create inline menu based on database by message id.
    '''
    msg_btns = await get_msg_btns(int(msg_id))

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for btn in msg_btns:
        if btn.button.func == 'open_msg':
            kb_builder.button(text=btn.button.content,
                              callback_data=f'open_msg:{btn.func_value}')
        elif btn.button.func == 'open_url':
            kb_builder.button(text=btn.button.content,
                              url=btn.func_value)

    kb_builder.adjust(1)

    return kb_builder.as_markup()
