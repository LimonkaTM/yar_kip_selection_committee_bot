from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ! temp database
from lexicon.msgs import btns, btns_msgs


#  Create inline menu for message
def create_msg_menu(msg_id: str) -> InlineKeyboardMarkup:
    '''
    Create inline menu based on database by message id.\n
    @param: msg_id Message id
    ! Need to rewrite with database
    '''
    msg_btns: dict = btns_msgs[msg_id]

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for btn_key in msg_btns:
        if btns[btn_key]['fn'] == 'open_msg':
            kb_builder.button(text=btns[btn_key]['content'], callback_data=f"open_msg:{msg_btns[btn_key]}")
        elif btns[btn_key]['fn'] == 'open_url':
            kb_builder.button(text=btns[btn_key]['content'], url=msg_btns[btn_key])

    kb_builder.adjust(1)

    return kb_builder.as_markup()
