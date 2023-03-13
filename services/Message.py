from peewee import fn

from models import Message


def get_all_messages() -> list[Message]:
    query = Message.select()

    return list(query)


def get_message(message_id: int) -> Message:
    return Message.get_or_none(Message.id == message_id)
