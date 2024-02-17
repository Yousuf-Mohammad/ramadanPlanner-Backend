from ninja.security import HttpBearer

from account.models import User
from account.utils import decode_token


class JWTAuth(HttpBearer):
    def authenticate(self, request, token: str):
        payload = decode_token(token)
        if payload and payload.get("type") == "access":
            user = User.objects.filter(id=payload["user_id"]).first()
            if not user:
                return None

            request.user = user
            return user
