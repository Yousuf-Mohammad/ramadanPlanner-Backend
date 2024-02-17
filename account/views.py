from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from ninja_extra import api_controller, http_get, http_patch, http_post

from account.models import User
from account.schemas import (
    AuthIn,
    AuthOut,
    AuthRefreshIn,
    PasswordIn,
    PasswordResetIn,
    PasswordResetRequestIn,
    ProfileIn,
    ProfileOut,
    RegisterIn,
)
from account.utils import create_access_token, create_refresh_token, decode_token
from common.enums import GenericStatus
from common.exceptions import BadRequestException, UnauthorizedException
from common.schemas import GenericSchemaOut


@api_controller("/auth", tags=["auth"], auth=None)
class AuthAPI:
    @http_post("register", response={201: GenericSchemaOut})
    def register(self, request, register_in: RegisterIn):
        if User.objects.filter(email=register_in.email).exists():
            raise BadRequestException("Email already taken")

        user = User.objects.create_user(
            email=register_in.email,
            password=register_in.password1,
            first_name=register_in.first_name,
            last_name=register_in.last_name,
        )

        if user:
            return GenericSchemaOut(message="Registration successful. Please login.")

        raise BadRequestException("Registration failed")

    @http_post("login", response=AuthOut)
    def login(self, request, auth_in: AuthIn):
        user = authenticate(email=auth_in.email, password=auth_in.password)
        if user:
            access_token = create_access_token(user_id=user.id)
            refresh_token = create_refresh_token(user_id=user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": user,
            }
        raise UnauthorizedException("Invalid credentials")

    @http_post("refresh", response=AuthOut)
    def refresh_login(self, request, refresh_in: AuthRefreshIn):
        payload = decode_token(refresh_in.refresh)
        if payload and payload.get("type") == "refresh":
            user = User.objects.filter(id=payload["user_id"]).first()
            if user:
                new_access_token = create_access_token(user_id=user.id)
                return {
                    "access_token": new_access_token,
                    "refresh_token": refresh_in.refresh,
                    "user": user,
                }
        raise UnauthorizedException("Invalid refresh token")

    @http_post("password-reset-request", response=GenericSchemaOut)
    def password_reset_request(self, request, reset_request_in: PasswordResetRequestIn):
        try:
            user = User.objects.get(email=reset_request_in.email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_url = f"{settings.FRONTEND_URL}/password-reset/{uid}/{token}/"

            send_mail(
                subject="Password Reset Request",
                message="Please go to the following link "
                f"to reset your password: {reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[reset_request_in.email],
            )
            return GenericSchemaOut(message="Password reset email sent.")

        except User.DoesNotExist:
            return GenericSchemaOut(message="Password reset email sent.")

    @http_post("password-reset", response=GenericSchemaOut)
    def password_reset(self, request, password_reset_in: PasswordResetIn):
        try:
            user_id = force_str(urlsafe_base64_decode(password_reset_in.uid))
            user = User.objects.get(pk=user_id)

            if default_token_generator.check_token(user, password_reset_in.token):
                user.set_password(password_reset_in.new_password1)
                user.save()
                return GenericSchemaOut(message="Password reset successful.")

            return GenericSchemaOut(message="Invalid token.")

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return GenericSchemaOut(message="Invalid user.")


@api_controller("/profile", tags=["profile"], permissions=[])
class ProfileAPI:
    @http_get(response=ProfileOut)
    def get_profile(self, request):
        return request.auth

    @http_patch(response=ProfileOut)
    def update_profile(self, request, profile_in: ProfileIn):
        profile = request.auth
        update_fields = {k: v for k, v in profile_in.dict().items() if v is not None}
        for field, value in update_fields.items():
            setattr(profile, field, value)
            setattr(profile, f"{field}_status", GenericStatus.PENDING.value)
        profile.save()
        return profile

    @http_patch("change-password", response=GenericSchemaOut)
    def change_password(self, request, password_in: PasswordIn):
        user = authenticate(email=request.auth.email, password=password_in.old_password)
        if user:
            user.set_password(password_in.new_password1)
            user.save()
            return GenericSchemaOut(message="Password updated successfully")
        raise UnauthorizedException("Invalid credentials")
