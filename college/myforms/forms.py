from django import forms
from django.core import validators

import os

random_str = lambda: os.urandom(10).hex()


#NOTE :         custom validators
def starts_with_a(value):
    if value[0].lower() != "a":
        raise forms.ValidationError("SURNAME must be start's with a")


class FirstForm(forms.Form):
    name = forms.CharField(initial="King", help_text="Your Name")
    email = forms.EmailField()
    contact_number = forms.CharField(max_length=14)
    key = forms.CharField(widget=forms.HiddenInput)


class SecondForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required": "Please enter your name"}, help_text="Your Full Name", label="Full Name", label_suffix="-")
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "first_class second_class", "id": "my_id"}))
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "5"}))
    
    dob = forms.DateField(widget=forms.DateInput)
    
    key = forms.CharField(initial=random_str, disabled=True)
    secret_id = forms.CharField(widget=forms.HiddenInput, initial=random_str)
    
    has_car = forms.CharField(widget=forms.CheckboxInput)
    image = forms.CharField(widget=forms.FileInput)


class ExampleForm(forms.Form):
    #!      default =>  strip=True
    # strip=False, empty_value="King"
    name = forms.CharField(min_length=4, max_length=30, error_messages={"required": "Please Enter Your Full Name"}, empty_value="aomthing")
    surname = forms.CharField(validators=[starts_with_a], required=False)
    
    agree = forms.BooleanField(required=False, label="Agree Conditions", label_suffix="")
    
    contact_number = forms.IntegerField(label="Contact Number", label_suffix=" : ", min_value=1, max_value=99, required=False)
    
    salary = forms.DecimalField(min_value=0, max_value=999, max_digits=5, decimal_places=2, required=False)
    
    rate = forms.FloatField(max_value=999, min_value=1, required=False)
    
    
    url = forms.URLField(required=False, empty_value="https://www.youtube.com/")
    email = forms.EmailField(required=False, empty_value="somthing@gmail.com")
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    c_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    description = forms.CharField(widget=forms.Textarea(attrs={"cols": 50, "rows": 5, "class": "first_class second_class"}), required=False)
    
    
    key = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(7)], required=False)
    
    
    def clean_name(self):
        # name_value = self.cleaned_data["name"]
        name_value = self.cleaned_data.get("name")
        
        if name_value[0].lower() != "a":
            raise forms.ValidationError("Name must be start's with a")
        return name_value
    
    def clean(self):
        cleaned_data = super().clean()
        
        email = self.cleaned_data["email"]
        url = self.cleaned_data["url"]
        
        password = self.cleaned_data["password"].lower()
        c_password = self.cleaned_data["c_password"].lower()
        
        
        if "gmail" not in email.lower():
            raise forms.ValidationError("Please enter valid email")
        
        if len(url) < 15:
            raise forms.ValidationError("URL must be greter than 15")
        
        if password != c_password:
            raise forms.ValidationError("Password and Confrim-Password didn't match")


class StyleForm(forms.Form):
    error_css_class = "thakur_arunesh"
    required_css_class = "required_class_arunesh"
    
    name = forms.CharField(min_length=4, max_length=20, error_messages={"required": "Enter Your Full Name..."})
    email = forms.EmailField(min_length=10, error_messages={"required": "Enter Your Valid Email Address..."})
    password = forms.CharField(error_messages={"required": "Enter Valid Password..."}) #! later convert to password and write strong password checker validator