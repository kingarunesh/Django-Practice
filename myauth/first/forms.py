from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class RegisterForm(UserCreationForm):
    #!      we can change anything in password field like this only
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        
        labels = {
            "email": "Email"
        }


class EditProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "last_login", "date_joined", "is_active"]
        
        labels = {
            "first_name": "First Name"
        }
        
        #!          not working
        # widgets = {
        #     "last_login": forms.DateTimeInput(disabled=True)
        # }


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        exclude = ("password",)