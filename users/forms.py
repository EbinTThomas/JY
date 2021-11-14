from .models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'user_name', 'email', 'password1', 'password2', 'phone', 'thumbnail']