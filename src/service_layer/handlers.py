from typing import Any
from typing import Callable

from core.messages import Command
from core.messages import Event
from core.unit_of_work import UnitOfWork

from src.domain import commands
from src.domain import models

COMMAND_HANDLERS: dict[type[Command], Callable[..., None]] = {}
EVENT_HANDLERS: dict[type[Event], list[Callable[..., None]]] = {}
