from models import Message
from loader import objects


async def get_message(msg_id: int) -> Message:
    '''
    Get message from database by message id
    '''
    return await objects.get(Message.select().where(Message.id == msg_id))


async def get_start_message() -> Message:
    '''
    Get message with type 'start' from database
    '''
    return await objects.get(Message.select().where(Message.type == 'start'))


async def get_help_message() -> Message:
    '''
    Get message with type 'help' from database
    '''
    return await objects.get(Message.select().where(Message.type == 'help'))
