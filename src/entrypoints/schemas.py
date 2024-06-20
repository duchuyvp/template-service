from datetime import date
from typing import Annotated

import fastapi
import pydantic


class RegisterEmailSchema(pydantic.BaseModel):
    email: str
    password: str
    re_password: str

    first_name: str = ""
    last_name: str = ""
    birthday: date = None
    address: str = ""


class RegisterPhoneNumberSchema(pydantic.BaseModel):
    phone_number: str
    password: str
    re_password: str

    first_name: str = ""
    last_name: str = ""
    birthday: date = None
    address: str = ""


class RegisterSSOSchema(pydantic.BaseModel):
    provider: str
    token: str


class VerifySchema(pydantic.BaseModel):
    otp_id: str
    otp: str


class LoginSchema(pydantic.BaseModel):
    email: str = ""
    phone_number: str = ""
    password: str
    device_id: Annotated[str, fastapi.Header(...)]


class LogoutSchema(pydantic.BaseModel):
    X_Token: Annotated[str, fastapi.Header(...)]
