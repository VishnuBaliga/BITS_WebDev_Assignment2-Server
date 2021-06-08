from django.http import JsonResponse
from rest_framework.views import exception_handler, APIView
from rest_framework.exceptions import (
    APIException as HttpInternalServerError, ValidationError as HttpBadRequest,
    AuthenticationFailed as HttpUnauthorized, PermissionDenied as HttpForbidden, NotFound as HttpNotFound)
from utils.exceptions import WSException


def map_ws_exception_to_http_exception(ex):
    exception_map = {
        400: HttpBadRequest,
        401: HttpUnauthorized,
        403: HttpForbidden,
        404: HttpNotFound
    }
    exc_class = exception_map.get(ex.status.value, HttpInternalServerError)
    exc_instance = exc_class(ex.message)
    exc_instance.__cause__ = ex  # exception chaining
    return exc_instance


def log(ex, context):
    request = context.get('request')
    view = context.get('view')
    if isinstance(view, APIView):
        view_name = view.__class__.__name__
    else:
        view_name = str(view)

    print(f"{view_name} {request.method} {request.get_full_path()} --data {request.data} => ERROR: {ex}")


def api_exception_handler(ex, context):
    if isinstance(ex, WSException):
        ex = map_ws_exception_to_http_exception(ex)
    log(ex, context)
    response = exception_handler(ex, context)
    if response is None:
        return JsonResponse({"status": "failed"}, status=500)
    return response
