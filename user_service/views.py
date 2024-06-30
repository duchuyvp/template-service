import json

import jwt
from core.unit_of_work import UnitOfWork

from user_service.domain import models


def get_token_encrypt(_id: str, uow: UnitOfWork) -> str:
    """get_token.

    Args:
        _id:

    Returns:
        str:
    """

    with uow:
        token = uow.repo.get(models.Token, message_id=_id)[0]  # type: models.Token
        value = token.encrypt()

    return {"token": value}


def get_token(id: str, uow: UnitOfWork) -> models.Token:
    """get_token.

    Args:
        id:
        uow:

    Returns:
        models.Token:
    """

    with uow:
        token = uow.repo.get(models.Token, id=id)[0]  # type: models.Token

    return token


def get_user(id: str, uow: UnitOfWork) -> models.User:
    """get_user.

    Args:
        id:
        uow:

    Returns:
        models.User:
    """

    with uow:
        user = uow.repo.get(models.User, id=id)[0]  # type: models.User

    return user
