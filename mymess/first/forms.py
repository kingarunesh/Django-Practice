from django import forms

from first.models import Aohan


class AohanForm(forms.ModelForm):
    class Meta:
        model = Aohan
        fields = "__all__"