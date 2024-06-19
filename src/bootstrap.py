"""
This module contains the bootstrap function for the allocation application.
"""

import inspect
import typing as t

from core import message_bus
from src.service_layer import handlers
from core.dependency_injection import inject_dependencies
from core.unit_of_work import UnitOfWork
from src.orm import start_mappers


def bootstrap(
    start_orm: bool = True,
    uow: UnitOfWork | type[UnitOfWork] = UnitOfWork,
) -> message_bus.MessageBus:
    """
    Bootstrap the allocation application.

    Args:
        start_orm: A boolean indicating whether to start the ORM.
        uow: An instance of the unit of work.
        publish: A callable for publishing events.

    Returns:
        An instance of the MessageBus.
    """
    if start_orm:
        start_mappers()

    if isinstance(uow, type):
        uow = uow()

    dependencies = {"uow": uow}
    injected_event_handlers = {
        event_type: [inject_dependencies(handler, dependencies) for handler in event_handlers]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies) for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return message_bus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )
