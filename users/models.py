from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import uuid
    
class CustomAccountManager(BaseUserManager):
  def create_user(self, email, user_name, password, **other_fields):
    if not email:
      raise ValueError(_('You must provide an email address'))
    email = self.normalize_email(email)
    user = self.model(email=email, user_name=user_name, **other_fields)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, user_name, password, **other_fields):
    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    other_fields.setdefault('is_active', True)

    if other_fields.get('is_staff') is not True:
      raise ValueError('Superuser must be assigned to is_staff=True.')
    
    if other_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must be assigned to is_superuser=True.')
    
    return self.create_user(email, user_name, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  email = models.EmailField(_('email address'), unique=True)
  user_name = models.CharField(max_length=150, unique=True)
  first_name = models.CharField(max_length=150, blank=True, null=True)
  last_name = models.CharField(max_length=150, blank=True, null=True)
  phone = PhoneNumberField(null=False, blank=False, unique=True)
  start_date = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = CustomAccountManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['user_name']

  def __str__(self):
      return self.user_name