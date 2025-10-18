from django import forms
from .models import Job, Profile


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
