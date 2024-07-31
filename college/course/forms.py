from django import forms

import os

random_id = lambda: os.urandom(5).hex()


class CourseForm(forms.Form):
    course_id = forms.CharField(initial=random_id, disabled=True)
    title = forms.CharField(error_messages={"required": "Title is require"})
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    email = forms.EmailField()