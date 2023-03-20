from models import MessageButton
from models import Button
from peewee import ModelSelect


def get_msg_btns(msg_id: int) -> ModelSelect:
    '''
    Get all message buttons from database by message id.\n
    
    '''
    return MessageButton.select(Button.content,
                                Button.func,
                                MessageButton.func_value).join(Button, attr='button').where(MessageButton.message == msg_id)
