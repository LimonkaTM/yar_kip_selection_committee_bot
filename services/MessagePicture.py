from models import MessagePicture


def get_all_message_pictures(message_id: int) -> list[MessagePicture]:
    return MessagePicture.select().where(MessagePicture.message == message_id)
