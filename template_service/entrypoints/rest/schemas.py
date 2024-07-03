from pydantic import BaseModel


class LoginResponseSchema(BaseModel):
    token: str
