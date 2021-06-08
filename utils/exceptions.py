from enum import Enum
from rest_framework.response import Response


class Status(Enum):
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


class WSException(Exception):
    """ Base exception class for all WS exceptions."""

    status = Status.INTERNAL_SERVER_ERROR
    message = ""
    detail = None

    def __init__(self, status=Status.INTERNAL_SERVER_ERROR, message="", detail=None):
        self.status = status or Status.INTERNAL_SERVER_ERROR
        self.message = message or ""
        self.detail = detail or None
        super().__init__(self.message)

    def __str__(self):
        detail = f"\nException Detail: {self.detail}" if self.detail else ""
        return f"{self.status.name} {self.message} {detail}"

    def http_response(self):
        return Response(data={"status": "failed", "message": self.message}, status=self.status.value)


class BadRequest(WSException):
    def __init__(self, message, **kwargs):
        super().__init__(Status.BAD_REQUEST, message, **kwargs)


class Unauthorized(WSException):
    def __init__(self, message, **kwargs):
        super().__init__(Status.UNAUTHORIZED, message, **kwargs)


class Forbidden(WSException):
    def __init__(self, message, **kwargs):
        super().__init__(Status.FORBIDDEN, message, **kwargs)


class NotFound(WSException):
    def __init__(self, message, **kwargs):
        super().__init__(Status.NOT_FOUND, message, **kwargs)


class Conflict(WSException):
    def __init__(self, message, **kwargs):
        super().__init__(Status.CONFLICT, message, **kwargs)
