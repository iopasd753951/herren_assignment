from rest_framework import viewsets

from accounts_api import models, serializers


class UserAccountViewSet(viewsets.ModelViewSet):
    """ 유저 생성, 업데이트 핸들러 """

    serializer_class = serializers.UserAccountSerializer
    queryset = models.UserAccount.objects.all()


class LoginViewSet(viewsets.ViewSet):
    """ 유저 로그인 이메일과 패스워드 """

    # serializers_class = AuthTokenSerializer