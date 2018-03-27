from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import uuid, datetime
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('User Must Have a Valid Username')
        account = self.model(
            username=self.model.normalize_username(username)
        )
        account.set_password(password)
        account.save()
        return account
    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account

class Account(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField('nombre', max_length=50, null=False, blank=False)
    last_name = models.CharField('apellido', max_length=50, null=False, blank=False)
    date_of_birth = models.DateField('Fecha de Naciemiento', null=True, blank=True)
    email = models.EmailField('correo electronico', null=True, blank=True)
    username = models.CharField('username',
    	max_length=40, null=False, unique=True, blank=False)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('superuser status', default=False)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return '{1} {2}'.format(self.name, self.last_name)
    
    def get_short_name(self):
        return self.username

    def age(self):
    	return int((datetime.datetime.now().date() - self.date_of_birth).days / 365.25)
