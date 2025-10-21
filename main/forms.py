from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        fields = ['location', 'skills', 'qualification']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3}),
        }
               

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']


