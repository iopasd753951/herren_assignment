from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserRegisterManager(BaseUserManager):
    """ 모델 매니저 """

    def create_user(self, email, name, password=None):
        """ 유저 생성 """

        if not email:
            raise ValueError("이메일을 적어주세요.")

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        """ 관리자 생성 """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_admin = True

        user.save(using=self._db)

        return user


class UserRegister(AbstractBaseUser):
    """ 유저 계정 모델 """

    email = models.EmailField(primary_key=True, verbose_name='이메일')
    name = models.CharField(max_length=20, verbose_name='사용자이름')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')

    objects = UserRegisterManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'
