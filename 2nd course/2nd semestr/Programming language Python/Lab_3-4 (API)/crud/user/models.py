from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user



class Users(AbstractBaseUser):
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True, blank=True)
    password = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_login = None
   
    objects = UserManager()


    def __str__(self):
        return f'{self.email}'