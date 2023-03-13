from peewee import AutoField, CharField, DateTimeField
# from loader import database
from .BaseModel import BaseModel
import datetime


class Message(BaseModel):
    id_message = AutoField()
    data = CharField(max_length=1024, null=False)
    type = CharField(max_length=50, null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)

    class Meta:
        db_table = 'Messages'
        # database = database
