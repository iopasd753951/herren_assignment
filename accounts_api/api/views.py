from rest_framework import viewsets

from . import serializers
from accounts_api import models


class UserAccountViewSet(viewsets.ModelViewSet):
    """ 유저 생성, 업데이트 핸들러 """

    serializer_class = serializers.UserAccountSerializer
    queryset = models.UserAccount.objects.all()


class LoginViewSet(viewsets.ViewSet):
    """ 유저 로그인 이메일과 패스워드 """
    pass