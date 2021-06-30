from .models import List
from django import forms

class CreditsForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('fullname','debt','sentinel','ai')

