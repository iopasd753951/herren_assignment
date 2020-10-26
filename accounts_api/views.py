from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings
from rest_framework.decorators import action

from . import models, serializers, permission


class UserAccountViewSet(viewsets.ModelViewSet):
    """ 유저 생성, 업데이트 핸들러 """

    serializer_class = serializers.UserAccountSerializer
    queryset = models.UserAccount.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnAccount,)

    @action(detail=True, methods=['post'])
    def leave(self, request):
        pass


class UserLoginApiView(ObtainAuthToken):
    """ 유저 로그인 이메일과 패스워드 """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserMailListViewSet(viewsets.ModelViewSet):
    """ 유저 메일 리스트 핸들러 """

    queryset = models.UserMailList.objects.all()
    serializer_class = serializers.UserMailListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnAccount,)
