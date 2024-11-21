from peewee import SqliteDatabase
from typing import Final

db: Final[SqliteDatabase] = SqliteDatabase("bot_data.sqlite")
