import dataclasses
from datetime import date
from datetime import datetime
from datetime import timedelta

import fastapi
import jwt
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
class Token(BaseModel):
    user_id: str = None
    expired_time: datetime = dataclasses.field(default_factory=lambda: datetime.now() + timedelta(days=1))
    expired: bool = False

    def encrypt(self):
        return jwt.encode(self.json, "my_super_very_secret_promax_samsung", algorithm="HS256")

    @classmethod
    def decrypt(cls, X_Token) -> "Token":
        try:
            payload = jwt.decode(X_Token, "my_super_very_secret_promax_samsung", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise fastapi.HTTPException(status_code=401, detail="Token has expired.")
        except jwt.InvalidTokenError:
            raise fastapi.HTTPException(status_code=401, detail="Invalid token.")
        return cls(**payload)


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
    user_id: str = None
    token: str = None
    expired_time: datetime = None
    expired: bool = False
    comment: str = ""
