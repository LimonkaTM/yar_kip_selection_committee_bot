from peewee import DateTimeField, ForeignKeyField, CompositeKey, TextField
from loader import db
from .BaseModel import BaseModel
from .Message import Message
from .Button import Button
import datetime


class MessageButton(BaseModel):
    message = ForeignKeyField(Message,
                              field='id',
                              on_delete='CASCADE',
                              on_update='CASCADE',
                              null=False)
    btn = ForeignKeyField(Button,
                          field='id',
                          on_delete='CASCADE',
                          on_update='CASCADE',
                          null=False)
    func_value = TextField(null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S',
                               null=False,
                               default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S',
                               null=False,
                               default=datetime.datetime.now)

    class Meta:
        table_name = 'Message_buttons'
        primary_key = CompositeKey('message', 'btn')
        database = db
