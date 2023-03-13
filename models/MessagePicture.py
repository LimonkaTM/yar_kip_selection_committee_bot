from peewee import (DateTimeField, ForeignKeyField, TextField, CompositeKey)

from .BaseModel import BaseModel
from .Message import Message


class MessagePicture(BaseModel):
    message = ForeignKeyField(Message, field='id_message', on_delete='CASCADE',
                              on_update='CASCADE', null=False)
    path = TextField(null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False)

    class Meta:
        db_table = 'MessagesPictures'
        primary_key = CompositeKey('message', 'path')
