from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class DataBase:
    name: str
    host: str
    port: int
    username: str
    password: str
    dir: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase


# Создаем функцию, которая будет читать файл .env и возвращать экземпляр
# класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(
                                int, env.list('ADMIN_IDS')))),
                  db=DataBase(name=env('DB_NAME'),
                              host=env('DB_HOST'),
                              port=env('DB_PORT'),
                              username=env('DB_USERNAME'),
                              password=env('DB_PASSWORD'),
                              dir=env('DIR')))
