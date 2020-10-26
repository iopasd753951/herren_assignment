from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from accounts_api import models


class UserAccountSerializer(serializers.ModelSerializer):
    """ 유저 계정 시리얼라이저 """

    class Meta:
        model = models.UserAccount
        fields = ('email', 'name', 'password', 'is_leave')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ (POST) 유저 생성 """

        user = models.UserAccount(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        """ 계정 정보수정 """

        query_set = models.UserAccount.objects.all()

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        if validated_data.is_leave:
            pass

        return super().update(instance, validated_data)


class LoginAuthTokenSerializer(serializers.Serializer):
    """ 로그인 시리얼라이저 """

    class Meta:
        model = models.UserAccount
        fields = {'email', 'password'}

    email = serializers.EmailField(label=_("email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserMailListSerializer(serializers.ModelSerializer):
    """ 유저 메일 리스트 시리얼라이저 """

    class Meta:
        model = models.UserMailList
        fields = ('id', 'added_email', 'added_name')

    def create(self, validated_data):
        """ (post) 메일링리스트에 추가 """
        if models.UserAccount.objects.filter(validated_data['added_email']).exists():
            if not models.UserMailList.objects.filter(validated_data['added_email']).exists():
                user = models.UserMailList(
                    added_email=validated_data['email'],
                    added_name=validated_data['name'],
                ).save()
            else:
                return "중복 에러메시지"
        else:
            return "존재하지않는 에러메세지"

        return user
