from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    #!      we can change anything in password field like this only
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        
        labels = {
            "email": "Email"
        }