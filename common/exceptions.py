from ninja.errors import HttpError


class BadRequestException(HttpError):
    """Exception raised for bad requests."""

    status_code = 400
    message = "Bad Request"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.status_code, self.message)


class UnauthorizedException(HttpError):
    """Exception raised for unauthorized requests."""

    status_code = 401
    message = "Unauthorized"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.status_code, self.message)


class NotFoundException(HttpError):
    """Exception raised for not found requests."""

    status_code = 404
    message = "Not Found"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.status_code, self.message)
