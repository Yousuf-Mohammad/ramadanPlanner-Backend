from ninja.security import HttpBearer

from account.models import User
from account.utils import decode_token


class JWTAuth(HttpBearer):
    def authenticate(self, request, token: str):
        payload = decode_token(token)
        if payload and payload.get("type") == "access":
            return User.objects.filter(id=payload["user_id"]).first()
