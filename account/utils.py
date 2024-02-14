from datetime import datetime, timedelta

import jwt
from django.conf import settings

from common.exceptions import BadRequestException


def create_access_token(user_id: int):
    payload = {
        "user_id": user_id,
        "type": "access",
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_DELTA),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_refresh_token(user_id: int):
    payload = {
        "user_id": user_id,
        "type": "refresh",
        "exp": datetime.utcnow()
        + timedelta(minutes=settings.JWT_REFRESH_EXPIRATION_DELTA),
    }
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def decode_token(token: str):
    try:
        return jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )

    except jwt.ExpiredSignatureError:
        raise BadRequestException("Token expired")

    except jwt.DecodeError:
        raise BadRequestException("Invalid token")
