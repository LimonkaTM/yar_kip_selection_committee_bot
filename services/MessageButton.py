from models import MessageButton
from models import Button
from loader import objects


async def get_msg_btns(msg_id: int):
    '''
    Get all message buttons from database by message id.\n
    '''
    # x = await objects.get(MessageButton.select(Button.content,
    #                                            Button.func,
    #                                            MessageButton.func_value).join(Button, attr='button').where(MessageButton.message == msg_id))
    return await objects.execute(MessageButton.select(Button.content,
                                                      Button.func,
                                                      MessageButton.func_value).join(Button, attr='button').where(MessageButton.message == msg_id))
