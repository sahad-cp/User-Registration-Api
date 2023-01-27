from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .manager import UserManager
# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email address', max_length=40, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True