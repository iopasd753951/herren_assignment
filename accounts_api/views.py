from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import models, serializers, permission


class UserAccountViewSet(viewsets.ModelViewSet):
    """ 유저 생성, 업데이트 핸들러 """

    serializer_class = serializers.UserAccountSerializer
    queryset = models.UserAccount.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnAccount,)


class UserLoginApiView(ObtainAuthToken):
    """ 유저 로그인 이메일과 패스워드 """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
