from django.contrib.auth.forms import  UserCreationForm #user creation forms
from django.contrib.auth.models import User # Import User model



#Create a User
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']