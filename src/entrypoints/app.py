import typing as t

import fastapi
from icecream import ic

from src.bootstrap import bootstrap
from src.domain.commands import TestCommand

bus = bootstrap()
app = fastapi.FastAPI()
