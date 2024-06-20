import typing as t

import fastapi
from icecream import ic

from src import views
from src.domain import commands
from src.domain import models
from src.entrypoints import schemas
from src.entrypoints.bus import bus
from src.entrypoints.depends import verify_token

app = fastapi.FastAPI()


@app.post("/register_email", status_code=fastapi.status.HTTP_201_CREATED)
async def register_email(schema: schemas.RegisterEmailSchema):
    command = commands.RegisterEmailCommand(
        email=schema.email,
        password=schema.password,
        re_password=schema.re_password,
        first_name=schema.first_name,
        last_name=schema.last_name,
        birthday=schema.birthday,
        address=schema.address,
    )
    bus.handle(command)
    return fastapi.Response(status_code=201)


@app.post("/register_phone_number", status_code=fastapi.status.HTTP_201_CREATED)
async def register_phone_number(schema: schemas.RegisterPhoneNumberSchema):
    command = commands.RegisterPhoneNumberCommand(
        phone_number=schema.phone_number,
        password=schema.password,
        re_password=schema.re_password,
        first_name=schema.first_name,
        last_name=schema.last_name,
        birthday=schema.birthday,
        address=schema.address,
    )
    bus.handle(command)
    return fastapi.Response(status_code=201)


@app.post("/verify", status_code=fastapi.status.HTTP_200_OK)
async def verify(schema: schemas.VerifySchema):
    command = commands.VerifyCommand(
        otp_id=schema.otp_id,
        otp=schema.otp,
    )
    bus.handle(command)
    return fastapi.Response(status_code=200)


@app.post("/login", status_code=fastapi.status.HTTP_200_OK)
async def login(schema: schemas.LoginSchema) -> str:
    command = commands.LoginCommand(
        email=schema.email,
        phone_number=schema.phone_number,
        password=schema.password,
        device_id=schema.device_id,
    )
    bus.handle(command)

    token = views.get_token_encrypt(command._id, uow=bus.uow)
    return token


@app.post("/login_success", status_code=fastapi.status.HTTP_200_OK)
async def login_success(user: models.User = fastapi.Depends(verify_token)) -> str:
    return f"Login success with User: {user.id}"


@app.post("/logout", status_code=fastapi.status.HTTP_200_OK)
async def logout(schema: schemas.LogoutSchema, user: models.User = fastapi.Depends(verify_token)):
    command = commands.LogoutCommand(
        X_Token=schema.X_Token,
    )
    bus.handle(command)
    return fastapi.Response(status_code=200)
