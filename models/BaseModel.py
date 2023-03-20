from peewee import Model

from loader import db


class BaseModel(Model):
    class Meta:
        databse = db
