from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from accounts.models import Profile
User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
    password_confirmation = forms.CharField(label="Re-enter your password", widget=forms.PasswordInput,
                                            strip=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise ValidationError('Passwords did not match')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
        labels = {'first_name': 'Name', 'last_name': 'Surname'}
