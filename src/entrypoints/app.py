import typing as t

import fastapi
from icecream import ic

from src.bootstrap import bootstrap
from src.domain import commands

bus = bootstrap()
app = fastapi.FastAPI()


@app.post("/register_email", status_code=fastapi.status.HTTP_201_CREATED)
async def register_email(command: commands.RegisterEmailCommand):
    bus.handle(command)
    return fastapi.Response(status_code=201)


@app.post("/register_phone_number", status_code=fastapi.status.HTTP_201_CREATED)
async def register_phone_number(command: commands.RegisterPhoneNumberCommand):
    bus.handle(command)
    return fastapi.Response(status_code=201)


@app.post("/verify", status_code=fastapi.status.HTTP_200_OK)
async def verify(command: commands.VerifyCommand):
    bus.handle(command)
    return fastapi.Response(status_code=200)
