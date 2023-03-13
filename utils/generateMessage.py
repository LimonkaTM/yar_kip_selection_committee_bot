from services.Message import get_message
from services.MessagePicture import get_all_message_pictures
from services.MessageButton import get_all_message_btns
from models import Message, MessageButton, MessagePicture

def generate_answer(message_id: int):
    message = generate_message()

def is_message_type_picture(message_type: str):
    return message_type == 'picture-message'


def is_message_type_message(message_type: str):
    return message_type == 'message'

def generate_message(message_id):
    message: Message = get_message(message_id)

    message_type = message.type

    if is_message_type_message(message_type):
        return 
