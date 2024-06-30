import logging
from typing import Any

import sqlalchemy as sa
from core.adapters import create_component_factory
from core.adapters import sqlalchemy_adapter
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Table
from user_service.settings import config
from sqlalchemy import event
from user_service.domain import models
import core
from core.orm import map_once

logger = logging.getLogger(__name__)


def setup_model_on_callbacks():
    def set_in_memory_attributes(obj: core.BaseModel, _):
        obj.load_from_database()

    for model in [
        models.OTP,
        models.PasswordReset,
        models.SocialMedia,
        models.Token,
        models.User,
    ]:
        event.listen(model, "load", set_in_memory_attributes)


component_factory = create_component_factory(config)
assert isinstance(component_factory, sqlalchemy_adapter.ComponentFactory)

registry = component_factory.create_orm_registry()


@map_once
def start_mappers() -> None:
    """
    This method starts the mappers.
    """

    users = Table(
        "users",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
        Column("email", String, unique=True),
        Column("phone_number", String, unique=True),
        Column("password", String),
        Column("first_name", String),
        Column("last_name", String),
        Column("email_verified", sa.Boolean),
        Column("phone_number_verified", sa.Boolean),
        Column("avatar", String),
        Column("birthday", Date),
        Column("address", String),
        Column("loyalty_score", sa.Float),
    )

    social_media = Table(
        "social_media",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
        Column("user_id", String),
        Column("provider", String),
        Column("token", String),
    )

    otp = Table(
        "otp",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
        Column("user_id", String),
        Column("email", String),
        Column("phone_number", String),
        Column("otp", String),
        Column("expired_time", DateTime),
        Column("verified", sa.Boolean),
        Column("expired", sa.Boolean),
        Column("comment", String),
    )

    password_reset = Table(
        "password_reset",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
        Column("user_id", String),
        Column("token", String),
        Column("expired_time", DateTime),
        Column("expired", sa.Boolean),
        Column("comment", String),
    )

    token = Table(
        "token",
        registry.metadata,
        Column("id", String, primary_key=True),
        Column("created_time", DateTime),
        Column("updated_time", DateTime),
        Column("message_id", String),
        Column("user_id", String),
        Column("expired_time", DateTime),
        Column("expired", sa.Boolean),
    )

    registry.map_imperatively(models.User, users)
    registry.map_imperatively(models.SocialMedia, social_media)
    registry.map_imperatively(models.OTP, otp)
    registry.map_imperatively(models.PasswordReset, password_reset)
    registry.map_imperatively(models.Token, token)

    setup_model_on_callbacks()

    assert isinstance(component_factory, sqlalchemy_adapter.ComponentFactory)
    registry.metadata.create_all(bind=component_factory.engine)
