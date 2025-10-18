from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Profile


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
