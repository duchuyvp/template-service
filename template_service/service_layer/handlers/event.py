import random
from hashlib import md5
from typing import Callable

from core.messages import Event
from core.unit_of_work import UnitOfWork

from template_service.domain import events
from template_service.domain import models


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
            otp=md5(code.encode()).hexdigest(),
            user_id=event.user_id,
            email=event.email,
            phone_number=event.phone_number,
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


EVENT_HANDLERS: dict[type[Event], list[Callable[..., None]]] = {
    events.UserCreatedEvent: [handle_user_created_event],
    events.OTPGeneratedEvent: [handle_otp_generated_event],
}
