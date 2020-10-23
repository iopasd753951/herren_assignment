from rest_framework import serializers

from accounts_api import models


class UserRegisterSerializer(serializers.ModelSerializer):
    model = models.UserRegister
