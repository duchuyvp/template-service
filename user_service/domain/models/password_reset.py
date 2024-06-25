from datetime import datetime
from datetime import timedelta

from core.models import BaseModel

__all__ = ["PasswordReset"]


class PasswordReset(BaseModel):
    user_id: str
    token: str
    expired_time: datetime
    expired: bool
    comment: str

    def __init__(self, user_id: str, token: str, *args, **kwargs):
        super().__init__()
        self.user_id = user_id
        self.token = token
        self.comment = f"Password reset token for {user_id}"
        self.expired_time = datetime.now() + timedelta(days=1)
        self.expired = False
