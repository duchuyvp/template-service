import dataclasses
from datetime import date

from core.models import BaseModel
from template_service.domain import events

__all__ = ["User"]


class User(BaseModel):
    email: str | None
    phone_number: str | None
    password: str
    first_name: str
    last_name: str
    avatar: str
    birthday: date = date(1970, 1, 1)
    address: str
    loyalty_score: float = 0.0
    email_verified: bool
    phone_number_verified: bool

    def __init__(
        self,
        password: str,
        email: str | None = None,
        phone_number: str | None = None,
        first_name: str = "",
        last_name: str = "",
        avatar: str = "",
        birthday: date = date.today(),
        address: str = "",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.birthday = birthday
        self.address = address
        self.email_verified = False
        self.phone_number_verified = False

    def __post_init__(self):
        self.events.append(events.UserCreatedEvent(user_id=self.id, email=self.email, phone_number=self.phone_number))
