from django import forms

import os

random_str = lambda: os.urandom(10).hex()


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