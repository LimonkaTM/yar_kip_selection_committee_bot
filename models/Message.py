from peewee import AutoField, DateTimeField, TextField, CharField
from loader import db
from .BaseModel import BaseModel
import datetime


class Message(BaseModel):
    id = AutoField()
    name = CharField(max_length=100,
                     null=False,
                     default='Имя сообщения')
    content = TextField(null=False)
    type = CharField(max_length=50,
                     null=False,
                     default='msg')
    photo = TextField(null=True)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S',
                               null=False,
                               default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S',
                               null=False,
                               default=datetime.datetime.now)

    class Meta:
        table_name = 'Messages'
        database = db
