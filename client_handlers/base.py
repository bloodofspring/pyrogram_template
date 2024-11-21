from datetime import datetime

from pyrogram.filters import command, regex, create
from pyrogram import Client, filters, types, handlers
from colorama import Fore

request_type = types.Message | types.CallbackQuery
__all__ = ["BaseHandler", "request_type", "Client", "command", "regex", "create"]


class BaseHandler:
    """Базовый обработчик-исполнитель"""
    __name__ = ""
    HANDLER: handlers.MessageHandler | handlers.CallbackQueryHandler = handlers.MessageHandler
    FILTER: filters.Filter | None = None

    def __init__(self):
        self.request: request_type | None = None
        self.client: Client | None = None

    async def func(self):
        raise NotImplementedError

    async def execute(self, client: Client, request: request_type):
        self.client = client
        self.request = request

        try:
            await self.func()
        except Exception as e:
            print(
                Fore.YELLOW + f"[{datetime.now()}][!]>>-||--> " +
                Fore.RED + f"Ошибка в {self.__name__}! [type={type(e)}; text={str(e)}]"
            )

    @property
    def de_pyrogram_handler(self):
        return self.HANDLER(self.func, self.FILTER)
