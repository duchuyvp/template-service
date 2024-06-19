import logging
from typing import Any

import sqlalchemy as sa
from core.adapters import create_component_factory
from core.adapters import sqlalchemy_adapter
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import orm
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import clear_mappers

from src.domain import models

logger = logging.getLogger(__name__)


def start_mappers(config: dict[str, Any] | None = None) -> None:
    """
    This method starts the mappers.
    """

    component_factory = create_component_factory(config)
    assert isinstance(component_factory, sqlalchemy_adapter.ComponentFactory)

    registry = component_factory.create_orm_registry()

    model_table = Table(
        "models",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
    )
    registry.map_imperatively(models.BaseModel, model_table)

    engine = component_factory.engine
    registry.metadata.create_all(bind=engine)
