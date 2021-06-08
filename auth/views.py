from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auth.serializers import UserProfileSerializer, UserAuthSerializer
from utils.messages import AuthMessages, BaseMessages


# Create your views here.


class UserLogin(generics.CreateAPIView):
    msg_ob = AuthMessages()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserAuthSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.created = datetime.now()
                token.save()
        else:
            response_context = {'resp_code': 0, 'status': 'Fail',
                                'message': self.msg_ob.login_failed, 'response': {}}
            return Response(response_context, status=status.HTTP_400_BAD_REQUEST)
        response_data = {'auth_token': token.key}
        response_context = {'resp_code': 1, 'status': 'success',
                            'message': self.msg_ob.login_success,
                            'response': response_data}
        return Response(response_context)


class UserRegistration(generics.CreateAPIView):
    msg_ob = BaseMessages()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
