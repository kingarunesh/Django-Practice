from django import forms

from students.models import Student



class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=8, required=False)
    
    class Meta:
        model = Student
        fields = ["name", "email", "password"]
        
        labels = {
            "name": "Full Name",
            "email": "Email Address",
        }
        
        help_text = {
            "name": "Enter Your Full Name"
        }
        
        error_messages = {
            "name": {"required": "Name is required field", "max_length": "Max is 10"},
            "email": {"required": "Email is required field", "unique": "Please enter unique email address"}
        }
        
        widgets = {
            "password": forms.PasswordInput,
            "name": forms.TextInput(attrs={"class": "first_class second_class", "placeholder": "Please Enter Name..."})
        }