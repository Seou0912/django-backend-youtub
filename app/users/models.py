from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class Usermanager(BaseUserManager):  # 유저를 생성하고 관리하는 역할
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # 비밀번호 해쉬화
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


# Create your models here.
# - email
# - password 따로 필요없음
# - nickname
# - is_business(boolean): personal, business


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)  # 여기까지 필요한 부분 생성

    is_active = models.BooleanField(default=True)  # 권한 관련 부분(인증)
    is_staff = models.BooleanField(default=False)  # 권한 관련 부분(인증)

    USERNAME_FIELD = "email"
    objects = Usermanager()

    def __str__(self):
        return f"email: {self.email}, nickname: {self.nickname}"
