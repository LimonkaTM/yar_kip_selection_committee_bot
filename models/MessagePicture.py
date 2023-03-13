from peewee import DateTimeField, ForeignKeyField, CharField, CompositeKey
# from loader import database
from .BaseModel import BaseModel
from .Message import Message
import datetime


class MessagePicture(BaseModel):
    message = ForeignKeyField(Message, field='id_message', on_delete='CASCADE',
                              on_update='CASCADE', null=False)
    path = CharField(max_length=100, null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)

    class Meta:
        db_table = 'MessagesPictures'
        primary_key = CompositeKey('message', 'path')
        # database = database
