from loader import database
from models import Message, MessageButton, MessagePicture
import time
# from peewee import (Model, SQL, AutoField, CharField, DateTimeField,
#                     ForeignKeyField, CompositeKey, TextField)

# # try:
# #     import playhouse.postgres_ext as pw_pext
# # except ImportError:
# #     pass


# def migrate(migrator, database, fake=False, **kwargs):

#     class BaseModel(Model):
#         class Meta:
#             databse = database

#     @migrator.create_model
#     class Message(BaseModel):
#         id = AutoField()
#         data = CharField(max_length=1024, null=False)
#         type = CharField(max_length=50, null=False)
#         created_at = DateTimeField(null=False)

#         class Meta:
#             db_table = 'Messages'

#     @migrator.create_model
#     class MessageButton(BaseModel):
#         message = ForeignKeyField(Message, field='id_message',
#                                   on_delete='CASCADE', on_update='CASCADE',
#                                   null=False)
#         type = CharField(max_length=50, null=False)
#         data = CharField(max_length=50, null=False)
#         function_data = CharField(max_length=50, null=False)
#         created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S', null=False)

#         class Meta:
#             db_table = 'MessagesButtons'
#             primary_key = CompositeKey('message', 'data')


# def rollback(migrator, database, fake=False, **kwargs):
#     """Write your rollback migrations here."""

#     migrator.remove_model('users')

#     migrator.remove_model('basemodel')

# with database:
#     database.drop_tables([MessageButton, Message, MessagePicture])
#     database.create_tables([MessageButton, Message, MessagePicture])
now = time.strftime('%Y-%m-%d %H:%M:%S')
# Message.create(data='Вас приветствует бот Приемной комиссии ГПОУ ЯО Ярославского колледжа индустрии питания. Здесь Вы сможете ознакомиться с основной информацией о приеме на текущий учебный год и узнать ответы на часто задаваемые вопросы.', 
#                type='message',
#                created_at=now,
#                updated_at=now)

# MessageButton.create(message=1,
#                      type='message-btn',
#                      data='Информация о приёме в текущем году',
#                      function_data='generate-message',
#                      created_at=now,
#                      updated_at=now)

# MessageButton.create(message=1,
#                      type='message-btn',
#                      data='Перевод из другого учбеного заведения',
#                      function_data='generate-message',
#                      created_at=now,
#                      updated_at=now)

# MessageButton.create(message=1,
#                      type='message-btn',
#                      data='FAQ',
#                      function_data='generate-message',
#                      created_at=now,
#                      updated_at=now)

# MessagePicture.create(message=1,
#                       path='logo_two_fix2.png',
#                       created_at=now,
#                       updated_at=now)
