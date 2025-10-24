from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Job


# ---------------------------
# USER REGISTRATION FORM
# ---------------------------
class CustomUserCreationForm(UserCreationForm):
    # Extra fields (not part of Django User model)
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    title = forms.ChoiceField(choices=Profile.TITLE_CHOICES, required=False)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True, help_text='Select your account type.')
    current_occupation = forms.CharField(max_length=100, required=False)
    remember_me = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = User
        # Only include fields that exist in the User model
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """Override save to also create a Profile object"""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            # Create the associated Profile record
            Profile.objects.create(
                user=user,
                title=self.cleaned_data.get('title', ''),
                current_occupation=self.cleaned_data.get('current_occupation', ''),
                role=self.cleaned_data['role']
            )
        return user


# ---------------------------
# PROFILE EDIT FORM
# ---------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'location', 'skills', 'qualification', 'current_occupation']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List your skills...'}),
            'qualification': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Relevant qualifications...'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., London, UK'}),
        }


# ---------------------------
# JOB MANAGEMENT FORM
# ---------------------------
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter job title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the job'}),
        }
