from django import forms

from crud.models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "password"]
        
        labels = {
            "name": "Full Name",
            "email": "Email Address",
            "password": "Password"
        }
        
        error_messages = {
            "name": {"required": "'name' field is require"},
            "email": {"required": "'email' field is require"},
            "password": {"required": "'password' field is require"},
        }
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }


"""
<div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
</div>
<div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" />
</div>
"""