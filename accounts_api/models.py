from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.contrib.auth import get_user_model


class UserAccountManager(BaseUserManager):
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
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """ 유저 계정 모델 """
    email = models.EmailField(primary_key=True, verbose_name='이메일')
    name = models.CharField(max_length=20, verbose_name='사용자이름')
    # email = models.CharField( max_length=200, verbose_name='이메일', unique=True)
    # name = models.CharField(max_length=20, verbose_name='사용자이름', primary_key=True)
    is_leave = models.BooleanField(default=False, verbose_name='탈퇴 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_staff = models.BooleanField(default=False, verbose_name='관리자 여부')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'accounts'

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email


class UserMailList(models.Model):
    """ 메일 리스트 모델 """
    user = models.ForeignKey(UserAccount, related_name='user_mail_list', on_delete=models.CASCADE)
    added_email = models.EmailField(verbose_name='추가할 이메일')
    added_name = models.CharField(max_length=20, verbose_name='추가할 사용자이름')
