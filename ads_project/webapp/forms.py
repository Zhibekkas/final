from django import forms
from webapp.models import Advertisement


class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ['author', 'is_moderated']
