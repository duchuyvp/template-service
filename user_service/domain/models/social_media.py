from core.models import BaseModel

__all__ = ["SocialMedia"]


class SocialMedia(BaseModel):
    user_id: str
    provider: str
    token: str

    def __init__(self, user_id: str, provider: str, token: str, *args, **kwargs):
        super().__init__()
        self.user_id = user_id
        self.provider = provider
        self.token = token
