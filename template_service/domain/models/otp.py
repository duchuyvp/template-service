from datetime import datetime

from core.models import BaseModel
from template_service.domain import events

__all__ = ["OTP"]


class OTP(BaseModel):
    user_id: str
    email: str | None
    phone_number: str | None
    otp: str
    expired_time: datetime
    expired: bool
    verified: bool
    comment: str

    def __init__(
        self,
        user_id: str,
        otp: str,
        email: str | None = None,
        phone_number: str | None = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.email = email
        self.phone_number = phone_number
        self.otp = otp
        self.expired = False
        self.verified = False
        self.comment = f"OTP for {user_id}"

    def __post_init__(self):
        self.events.append(events.OTPGeneratedEvent(code=self.otp, email=self.email, phone_number=self.phone_number))
