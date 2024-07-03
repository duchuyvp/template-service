import dataclasses
from datetime import datetime
from datetime import timedelta

import fastapi
import jwt
from core.models import BaseModel

__all__ = ["Token"]


class Token(BaseModel):
    user_id: str
    expired_time: datetime = dataclasses.field(default_factory=lambda: datetime.now() + timedelta(days=1))
    expired: bool

    def __init__(self, user_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.expired = False

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
