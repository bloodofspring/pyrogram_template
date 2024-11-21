import json
from typing import Final

from dotenv import load_dotenv
from os import environ

load_dotenv()

ADMINS: Final[list[int]] = json.loads(environ["admins"])
