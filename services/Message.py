from models import Message


def get_message(msg_id: int) -> Message:
    '''
    Get message from database by message id
    '''
    return Message.get_or_none(Message.id == msg_id)


def get_start_message() -> Message:
    '''
    Get message with type 'start' from database
    '''
    return Message.get_or_none(Message.type == 'start')


def get_help_message() -> Message:
    '''
    Get message with type 'help' from database
    '''
    return Message.get_or_none(Message.type == 'help')
