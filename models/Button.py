from peewee import CharField, DateTimeField, AutoField
from loader import db
from .BaseModel import BaseModel
import datetime


class Button(BaseModel):
    id = AutoField()
    content = CharField(max_length=1024, null=False)
    func = CharField(max_length=50, default='open_msg', null=False)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)
    updated_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False, default=datetime.datetime.now)

    class Meta:
        table_name = 'Buttons'
        database = db
