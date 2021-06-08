import abc

from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from .exceptions import WSException, Unauthorized


class WSBaseAuthentication(BaseAuthentication):
    def __init__(self, realm="API"):
        self.realm = realm

    def authenticate(self, request, **kwargs):
        try:
            auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
            _, auth_token = self.get_auth_header(auth_header_value)

            if not auth_token:
                raise Unauthorized(f"Invalid authorization header='{auth_header_value}'")

            authenticated_user = self.get_auth_user(auth_token)

            return authenticated_user, None
        except WSException as ex:
            if self.should_raise(request):
                raise ex
            return None
        except Exception as ex:
            request.user = AnonymousUser()
            # deliberately suppressing message since we don't want unexpected exception message escaping to response
            raise Unauthorized("unexpected exception") from ex

    def should_raise(self, request):
        last_authenticator = request.authenticators[-1]
        return self == last_authenticator

    @abc.abstractmethod
    def get_auth_user(self, auth_token):
        pass

    @abc.abstractmethod
    def get_auth_header(self, auth_header_value):
        pass


