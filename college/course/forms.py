from django import forms

from course.models import Member

import os
random_id = lambda: os.urandom(5).hex()


class CourseForm(forms.Form):
    course_id = forms.CharField(initial=random_id, disabled=True)
    title = forms.CharField(error_messages={"required": "Title is require"})
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    email = forms.EmailField()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["teacher_name", "contact_number", "email", "joined_date"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["student_name", "contact_number", "email", "joined_date"]