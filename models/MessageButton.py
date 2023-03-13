from peewee import CharField, DateTimeField, ForeignKeyField, CompositeKey
# from loader import database
from .BaseModel import BaseModel
from .Message import Message
import datetime


class MessageButton(BaseModel):
    message = ForeignKeyField(Message, field='id_message', on_delete='CASCADE',
                              on_update='CASCADE', null=False)
    type = CharField(max_length=50, null=False)
    data = CharField(max_length=50, null=False)
    function_data = CharField(max_length=50, null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)

    class Meta:
        db_table = 'MessagesButtons'
        primary_key = CompositeKey('message', 'data')
        # database = database
