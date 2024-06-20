import random
from hashlib import md5
from typing import Any
from typing import Callable

from core.messages import Command
from core.messages import Event
from core.unit_of_work import UnitOfWork

from src.domain import commands
from src.domain import events
from src.domain import models


def handle_register_email_command(command: commands.RegisterEmailCommand, uow: UnitOfWork) -> None:
    """handle_register_email_command.

    Args:
        command:
        uow:
    """
    with uow:
        if command.password != command.re_password:
            raise ValueError("Passwords do not match.")
        user = models.User(
            message_id=command._id,
            email=command.email,
            password=command.password,
            first_name=command.first_name,
            last_name=command.last_name,
            birthday=command.birthday,
            address=command.address,
        )
        uow.repo.add(user)
        uow.commit()


def handle_register_phone_number_command(command: commands.RegisterPhoneNumberCommand, uow: UnitOfWork) -> None:
    """handle_register_phone_number_command.

    Args:
        command:
        uow:
    """
    with uow:
        if command.password != command.re_password:
            raise ValueError("Passwords do not match.")
        user = models.User(
            message_id=command._id,
            phone_number=command.phone_number,
            password=command.password,
            first_name=command.first_name,
            last_name=command.last_name,
            birthday=command.birthday,
            address=command.address,
        )
        uow.repo.add(user)
        uow.commit()


def handle_user_created_event(event: events.UserCreatedEvent, uow: UnitOfWork) -> None:
    """handle_user_created_event.

    Args:
        event:
        uow:
    """
    with uow:
        code = str(random.randint(100000, 999999))
        otp = models.OTP(
            message_id=event._id,
            user_id=event.user_id,
            email=event.email,
            phone_number=event.phone_number,
            otp=md5(code.encode()).hexdigest(),
        )
        uow.repo.add(otp)
        uow.commit()
        # otp.events.append(models.OTPGeneratedEvent(otp_id=otp.id))


def handle_otp_generated_event(event: events.OTPGeneratedEvent, uow: UnitOfWork) -> None:
    """handle_otp_generated_event.

    Args:
        event:
        uow:
    """
    with uow:
        if event.email:
            # send email
            ...
        elif event.phone_number:
            # send sms
            ...

        # assume that the OTP has been sent to the user


def handle_verify_command(command: commands.VerifyCommand, uow: UnitOfWork) -> None:
    """handle_verify_command.

    Args:
        command:
        uow:
    """
    with uow:
        otp = uow.repo.get(models.OTP, id=command.otp_id)[0]
        if otp.otp != md5(command.otp.encode()).hexdigest():  # type: ignore
            raise ValueError("Invalid OTP.")
        otp.verified = True
        uow.commit()


COMMAND_HANDLERS: dict[type[Command], Callable[..., None]] = {
    commands.RegisterEmailCommand: handle_register_email_command,
    commands.RegisterPhoneNumberCommand: handle_register_phone_number_command,
}
EVENT_HANDLERS: dict[type[Event], list[Callable[..., None]]] = {
    events.UserCreatedEvent: [handle_user_created_event],
    events.OTPGeneratedEvent: [handle_otp_generated_event],
}
