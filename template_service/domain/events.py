from core.messages import Event


class UserCreatedEvent(Event):
    """
    UserCreatedEvent.
    """

    user_id: str
    email: str | None
    phone_number: str | None


class OTPGeneratedEvent(Event):
    """
    OTPGeneratedEvent.
    """

    code: str
    email: str | None
    phone_number: str | None
