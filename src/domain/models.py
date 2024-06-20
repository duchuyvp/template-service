import dataclasses
from datetime import date
from datetime import datetime

from core.models import BaseModel

from src.domain import events


@dataclasses.dataclass(init=True)
class User(BaseModel):
    email: str = None
    phone_number: str = None
    password: str = None
    first_name: str = None
    last_name: str = None
    avatar: str = None
    birthday: date = None
    address: str = None
    loyalty_score: float = 0.0
    email_verified: bool = False
    phone_number_verified: bool = False

    def __post_init__(self):
        self.events.append(events.UserCreatedEvent(user_id=self.id, email=self.email, phone_number=self.phone_number))


@dataclasses.dataclass(init=True)
class SocialMedia(BaseModel):
    user_id: str = None
    provider: str = None
    token: str = None


@dataclasses.dataclass(init=True)
class OTP(BaseModel):
    user_id: str = None
    email: str | None = None
    phone_number: str | None = None
    otp: str = None
    expired_time: datetime = None
    expired: bool = False
    verified: bool = False
    comment: str = ""

    def __post_init__(self):
        self.events.append(events.OTPGeneratedEvent(code=self.otp, email=self.email, phone_number=self.phone_number))


@dataclasses.dataclass(init=True)
class PasswordReset(BaseModel):
    user_id: str
    token: str
    expired_time: datetime
    expired: bool
    comment: str
