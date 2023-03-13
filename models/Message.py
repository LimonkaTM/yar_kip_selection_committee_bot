from peewee import AutoField, CharField, DateTimeField

from .BaseModel import BaseModel


class Message(BaseModel):
    id = AutoField()
    data = CharField(max_length=1024, null=False)
    type = CharField(max_length=50, null=False)
    created_at = DateTimeField(null=False)

    class Meta:
        db_table = 'Messages'
