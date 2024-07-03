"""
This module contains the bootstrap function for the allocation application.
"""

from core import MessageBus
from core.dependency_injection import inject_dependencies
from core.unit_of_work import UnitOfWork
from template_service.adapters.orm import start_mappers
from template_service.service_layer.handlers import command
from template_service.service_layer.handlers import event


def bootstrap(
    start_orm: bool = True,
    uow: UnitOfWork | type[UnitOfWork] = UnitOfWork,
) -> MessageBus:
    """
    Bootstrap the allocation application.

    Args:
        start_orm: A boolean indicating whether to start the ORM.
        uow: An instance of the unit of work.

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
        for event_type, event_handlers in event.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies) for command_type, handler in command.COMMAND_HANDLERS.items()
    }

    return MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )
