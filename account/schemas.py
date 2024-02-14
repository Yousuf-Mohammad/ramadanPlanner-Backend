from typing import Any

from ninja import ModelSchema, Schema
from ninja.errors import ValidationError
from pydantic import EmailStr, field_validator

from account.models import User


class RegisterIn(ModelSchema):
    email: EmailStr

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

    password1: str
    password2: str

    @field_validator("password2")
    def passwords_match(cls, v, values, **kwargs) -> Any:
        if "password1" in values.data and v != values.data["password1"]:
            raise ValidationError("Passwords do not match")
        return v


class UserOut(ModelSchema):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class AuthIn(Schema):
    email: EmailStr
    password: str


class AuthRefreshIn(Schema):
    refresh: str


class AuthOut(Schema):
    access_token: str
    refresh_token: str
    user: UserOut


class ProfileIn(ModelSchema):
    email: EmailStr = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class ProfileOut(ModelSchema):
    class Meta:
        model = User
        exclude = [
            "password",
            "groups",
            "user_permissions",
        ]


class PasswordIn(Schema):
    old_password: str
    new_password1: str
    new_password2: str

    @field_validator("new_password2")
    def passwords_match(cls, v, values, **kwargs) -> Any:
        if "new_password1" in values.data and v != values.data["new_password1"]:
            raise ValidationError("Passwords do not match")
        return v


class PasswordResetRequestIn(Schema):
    email: str


class PasswordResetIn(Schema):
    uid: str
    token: str
    new_password1: str
    new_password2: str

    @field_validator("new_password2")
    def passwords_match(cls, v, values, **kwargs) -> Any:
        if "new_password1" in values.data and v != values.data["new_password1"]:
            raise ValidationError("Passwords do not match")
        return v
