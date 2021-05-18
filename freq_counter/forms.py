from django import forms

from .models import Url_mod

class Url_form(forms.ModelForm):
    class Meta:
        model=Url_mod
        fields = ["url"]