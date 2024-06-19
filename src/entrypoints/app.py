import typing as t

import fastapi
from icecream import ic

from src.domain.commands import TestCommand
from src.bootstrap import bootstrap

bus = bootstrap()
app = fastapi.FastAPI()
