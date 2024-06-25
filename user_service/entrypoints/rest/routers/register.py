import fastapi
from user_service.domain import commands

from .bus import bus

router = fastapi.APIRouter()


@router.post("/register_email", status_code=fastapi.status.HTTP_201_CREATED)
async def register_email(command: commands.RegisterEmailCommand):
    bus.handle(command)
    return fastapi.Response(status_code=201)


@router.post("/register_phone_number", status_code=fastapi.status.HTTP_201_CREATED)
async def register_phone_number(command: commands.RegisterPhoneNumberCommand):
    bus.handle(command)
    return fastapi.Response(status_code=201)


@router.post("/verify", status_code=fastapi.status.HTTP_200_OK)
async def verify(command: commands.VerifyCommand):
    bus.handle(command)
    return fastapi.Response(status_code=200)
