import fastapi
import jwt

from src import views
from src.domain import models
from src.entrypoints.bus import bus


def verify_token(X_Token: str = fastapi.Header(...)):
    """verify_token.

    Args:
        X_Token:

    Returns:
        str:
    """

    payload = models.Token.decrypt(X_Token)
    token = views.get_token(id=payload.id, uow=bus.uow)

    if not token:
        raise fastapi.HTTPException(status_code=401, detail="Fake token.")

    if token.expired or token.expired_time < token.expired_time.now():  # =))))
        raise fastapi.HTTPException(status_code=401, detail="Token has expired.")

    user = views.get_user(id=token.user_id, uow=bus.uow)

    return user
