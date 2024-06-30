import http
from datetime import datetime
from typing import Optional

import fastapi
from icecream import ic

from user_service import views
from user_service.domain import commands, models
from user_service.entrypoints.rest import schemas
from .bus import bus

router = fastapi.APIRouter()


# depends.py
def verify_token(X_Token: str = fastapi.Header(...)):
    """verify_token.

    This function is used to verify the token, for purpose for test only,
    and will be remove when Autneticate service is ready.

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


@router.post("/login", status_code=fastapi.status.HTTP_200_OK)
async def login(command: commands.LoginCommand) -> schemas.LoginResponseSchema:
    bus.handle(command)

    token = views.get_token_encrypt(command._id, uow=bus.uow)
    return token


@router.post("/login_success", status_code=fastapi.status.HTTP_200_OK)
async def login_success(user: models.User = fastapi.Depends(verify_token)) -> str:
    return f"Login success with User: {user.id}"


@router.post("/logout", status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def logout(command: commands.LogoutCommand):
    bus.handle(command)
    return fastapi.Response(status_code=200)
