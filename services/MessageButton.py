from models import MessageButton


def get_all_message_btns(message_id: int) -> list[MessageButton]:
    return MessageButton.select().where(MessageButton.message == message_id)
