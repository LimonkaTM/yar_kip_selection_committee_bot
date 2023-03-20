from loader import db
from models import Message, MessageButton, Button, BaseModel
from lexicon.lexicon import LEXICON_DATA, LEXICON_BUTTONS
import time
from services.MessageButton import get_msg_btns
from services.Message import get_message
from services.Button import get_all_btns

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

with db:
    db.drop_tables([MessageButton, Message, Button])
    db.create_tables([MessageButton, Message, Button])
now = time.strftime('%Y-%m-%d %H:%M:%S')

for key in LEXICON_DATA:
    print(key)
    if key == '1':
        Message.create(content=str(LEXICON_DATA[key]),
                       name='Сообщение запуска',
                       type='start',
                       photo='D:\\Documents\\Programing\\Python\\yar_kip_selection_committee_bot\\assets\\start_logo.png',
                       created_at=now,
                       updated_at=now)
    elif key == 'help':
        Message.create(content=str(LEXICON_DATA[key]),
                       name='Справка пользователя',
                       type='help',
                       created_at=now,
                       updated_at=now)
    else:
        Message.create(content=str(LEXICON_DATA[key]),
                       type='msg',
                       created_at=now,
                       updated_at=now)

for key in LEXICON_BUTTONS:
    if key == 'certificates-rating':
        Button.create(content=LEXICON_BUTTONS[key],
                      func='open_url',
                      created_at=now,
                      updated_at=now)
    else:
        Button.create(content=LEXICON_BUTTONS[key],
                      func='open_msg',
                      created_at=now,
                      updated_at=now)

# start
# Информация о приёме
MessageButton.create(message=1,
                     btn=1,
                     func_value=2,
                     created_at=now,
                     updated_at=now)
# Информация о прееводе
MessageButton.create(message=1,
                     btn=2,
                     func_value=23,
                     created_at=now,
                     updated_at=now)
# Платные образовательные услуги
MessageButton.create(message=1,
                     btn=3,
                     func_value=24,
                     created_at=now,
                     updated_at=now)
# Рейтинг аттестатов (ссылка)
MessageButton.create(message=1,
                     btn=4,
                     func_value='https://yar-kip.edu.yar.ru/abiturientam/plan_priema.html',
                     created_at=now,
                     updated_at=now)
# FAQ
MessageButton.create(message=1,
                     btn=5,
                     func_value=25,
                     created_at=now,
                     updated_at=now)

# Сообщение: Информация о приёме
# Порядок поступления
MessageButton.create(message=2,
                     btn=6,
                     func_value=19,
                     created_at=now,
                     updated_at=now)
# Перечень специальностей и профессий
MessageButton.create(message=2,
                     btn=7,
                     func_value=3,
                     created_at=now,
                     updated_at=now)
# Сроки подачи документов
MessageButton.create(message=2,
                     btn=8,
                     func_value=20,
                     created_at=now,
                     updated_at=now)
# Сроки подачи документов (назад)
MessageButton.create(message=20,
                     btn=26,
                     func_value=2,
                     created_at=now,
                     updated_at=now)
# Способы подачи документов
MessageButton.create(message=2,
                     btn=9,
                     func_value=21,
                     created_at=now,
                     updated_at=now)
# Способы подачи документов (назад)
MessageButton.create(message=21,
                     btn=26,
                     func_value=2,
                     created_at=now,
                     updated_at=now)
# Социальные льготы
MessageButton.create(message=2,
                     btn=10,
                     func_value=22,
                     created_at=now,
                     updated_at=now)
# Социальные льготы (назад)
MessageButton.create(message=22,
                     btn=26,
                     func_value=2,
                     created_at=now,
                     updated_at=now)
# Назад
MessageButton.create(message=2,
                     btn=26,
                     func_value=1,
                     created_at=now,
                     updated_at=now)

# Информация о переводе
# Назад
MessageButton.create(message=23,
                     btn=26,
                     func_value=1,
                     created_at=now,
                     updated_at=now)

# Платные образовательные услуги
# Назад
MessageButton.create(message=24,
                     btn=26,
                     func_value=1,
                     created_at=now,
                     updated_at=now)

# FAQ
# Назад
MessageButton.create(message=25,
                     btn=26,
                     func_value=1,
                     created_at=now,
                     updated_at=now)
# Предоставляется ли общажитие
MessageButton.create(message=25,
                     btn=17,
                     func_value=26,
                     created_at=now,
                     updated_at=now)
# # Мед книжка
# MessageButton.create(message=25,
#                      btn=26,
#                      func_value=27,
#                      created_at=now,
#                      updated_at=now)
# # О сборах
# MessageButton.create(message=25,
#                      btn=26,
#                      func_value=28,
#                      created_at=now,
#                      updated_at=now)
# # Какой корпус
# MessageButton.create(message=25,
#                      btn=26,
#                      func_value=29,
#                      created_at=now,
#                      updated_at=now)

# Назад (общежитие)
MessageButton.create(message=26,
                     btn=26,
                     func_value=25,
                     created_at=now,
                     updated_at=now)
# Назад(порядок поступления)
MessageButton.create(message=19,
                     btn=26,
                     func_value=2,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (мци)
MessageButton.create(message=3,
                     btn=18,
                     func_value=16,
                     created_at=now,
                     updated_at=now)
# МЦИ (подробнее)
MessageButton.create(message=16,
                     btn=24,
                     func_value=17,
                     created_at=now,
                     updated_at=now)
# МЦИ (подробнее - назад)
MessageButton.create(message=17,
                     btn=26,
                     func_value=16,
                     created_at=now,
                     updated_at=now)
# МЦИ (доки)
MessageButton.create(message=16,
                     btn=25,
                     func_value=18,
                     created_at=now,
                     updated_at=now)
# МЦИ (доки - назад)
MessageButton.create(message=18,
                     btn=26,
                     func_value=16,
                     created_at=now,
                     updated_at=now)
# МЦИ (назад)
MessageButton.create(message=16,
                     btn=26,
                     func_value=3,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (повар, кондитер)
MessageButton.create(message=3,
                     btn=19,
                     func_value=13,
                     created_at=now,
                     updated_at=now)
# Повар, кондитер (подробнее)
MessageButton.create(message=13,
                     btn=24,
                     func_value=14,
                     created_at=now,
                     updated_at=now)
# Повар, кондитер (подробнее - назад)
MessageButton.create(message=14,
                     btn=26,
                     func_value=13,
                     created_at=now,
                     updated_at=now)
# Повар, кондитер (доки)
MessageButton.create(message=13,
                     btn=25,
                     func_value=15,
                     created_at=now,
                     updated_at=now)
# Повар, кондитер (доки - назад)
MessageButton.create(message=15,
                     btn=26,
                     func_value=13,
                     created_at=now,
                     updated_at=now)
# Повар, кондитер (назад)
MessageButton.create(message=13,
                     btn=26,
                     func_value=3,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (поварское и кондитерское дело)
MessageButton.create(message=3,
                     btn=20,
                     func_value=4,
                     created_at=now,
                     updated_at=now)
# поварское и кондитерское дело (подробнее)
MessageButton.create(message=4,
                     btn=24,
                     func_value=5,
                     created_at=now,
                     updated_at=now)
# поварское и кондитерское дело (подробнее - назад)
MessageButton.create(message=5,
                     btn=26,
                     func_value=4,
                     created_at=now,
                     updated_at=now)
# поварское и кондитерское дело (доки)
MessageButton.create(message=4,
                     btn=25,
                     func_value=6,
                     created_at=now,
                     updated_at=now)
# поварское и кондитерское дело (доки - назад)
MessageButton.create(message=6,
                     btn=26,
                     func_value=4,
                     created_at=now,
                     updated_at=now)
# поварское и кондитерское дело (назад)
MessageButton.create(message=4,
                     btn=26,
                     func_value=3,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (сетевое и системное администрир)
MessageButton.create(message=3,
                     btn=21,
                     func_value=2,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (технология хлеба)
MessageButton.create(message=3,
                     btn=22,
                     func_value=10,
                     created_at=now,
                     updated_at=now)
# технология хлеба (подробнее)
MessageButton.create(message=10,
                     btn=24,
                     func_value=11,
                     created_at=now,
                     updated_at=now)
# технология хлеба (подробнее - назад)
MessageButton.create(message=11,
                     btn=26,
                     func_value=10,
                     created_at=now,
                     updated_at=now)
# технология хлеба (доки)
MessageButton.create(message=10,
                     btn=25,
                     func_value=12,
                     created_at=now,
                     updated_at=now)
# технология хлеба (доки - назад)
MessageButton.create(message=12,
                     btn=26,
                     func_value=10,
                     created_at=now,
                     updated_at=now)
# технология хлеба (назад)
MessageButton.create(message=10,
                     btn=26,
                     func_value=3,
                     created_at=now,
                     updated_at=now)

# Спиосок профессий (экономика)
MessageButton.create(message=3,
                     btn=23,
                     func_value=7,
                     created_at=now,
                     updated_at=now)
# экономика (подробнее)
MessageButton.create(message=7,
                     btn=24,
                     func_value=8,
                     created_at=now,
                     updated_at=now)
# экономика (подробнее - назад)
MessageButton.create(message=8,
                     btn=26,
                     func_value=7,
                     created_at=now,
                     updated_at=now)
# экономика (доки)
MessageButton.create(message=7,
                     btn=25,
                     func_value=9,
                     created_at=now,
                     updated_at=now)
# экономика (доки - назад)
MessageButton.create(message=9,
                     btn=26,
                     func_value=7,
                     created_at=now,
                     updated_at=now)
# экономика (назад)
MessageButton.create(message=7,
                     btn=26,
                     func_value=3,
                     created_at=now,
                     updated_at=now)

# Список профессий (назад)
MessageButton.create(message=3,
                     btn=26,
                     func_value=2,
                     created_at=now,
                     updated_at=now)

# /help (назад)
MessageButton.create(message=30,
                     btn=27,
                     func_value=1,
                     created_at=now,
                     updated_at=now)
