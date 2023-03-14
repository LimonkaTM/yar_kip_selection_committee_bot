from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from peewee import SqliteDatabase, MySQLDatabase

from config_data.config import Config, load_config

config: Config = load_config()

bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

storage = MemoryStorage()

if config.db.username and config.db.password and config.db.host and config.db.port and config.db.name:
    database = MySQLDatabase(config.db.name, user=config.db.username, password=config.db.password,
                             host=config.db.host, port=int(config.db.port))
else:
    database = SqliteDatabase(f'{config.db.dir}/database.sqlite3')

dp = Dispatcher(storage=storage)