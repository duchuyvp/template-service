from datetime import date

import pydantic
from core.messages import Command


class RegisterEmailCommand(Command):
    """
    RegisterEmailCommand.
    """

    email: str
    password: str
    re_password: str

    first_name: str = ""
    last_name: str = ""
    birthday: date = pydantic.Field(default_factory=date.today)
    address: str = ""


class RegisterPhoneNumberCommand(Command):
    """
    RegisterPhoneNumberCommand.
    """

    phone_number: str
    password: str
    re_password: str

    first_name: str = ""
    last_name: str = ""
    birthday: date = pydantic.Field(default_factory=date.today)
    address: str = ""


class RegisterSSOCommand(Command):
    """ """

    provider: str
    token: str


class VerifyCommand(Command):
    """ """

    otp_id: str
    otp: str


class LoginCommand(Command):
    """ """

    email: str = ""
    phone_number: str = ""
    password: str
    device_id: str = ""


class LogoutCommand(Command):
    """ """

    X_Token: str
