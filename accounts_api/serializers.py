from rest_framework import serializers

from accounts_api import models


class UserAccountSerializer(serializers.ModelSerializer):
    """ 유저 계정 시리얼라이저 """

    class Meta:
        model = models.UserAccount
        fields = ('email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ (POST) 유저 생성 """

        user = models.UserAccount(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
