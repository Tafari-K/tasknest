from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Job, ROLE_CHOICES


# ---------------------------
# TRADE OPTIONS (for Tradesmen)
# ---------------------------
TRADE_CHOICES = [
    ('plumber', 'Plumber'),
    ('electrician', 'Electrician'),
    ('carpenter', 'Carpenter'),
    ('painter', 'Painter'),
    ('handyman', 'Handyman'),
]

# ---------------------------
# USER REGISTRATION FORM
# ---------------------------


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True, help_text='Select your account type.',
        initial='customer')
    current_occupation = forms.ChoiceField(
        choices=TRADE_CHOICES,
        required=False,
        label="Trade Specialism (if applicable)"
    )

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']

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
                role=self.cleaned_data['role']
            )
        return user


# ---------------------------
# PROFILE EDIT FORM
# ---------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role',
                  'location',
                  'skills',
                  'qualification',
                  'current_occupation']
        widgets = {
            'skills': forms.Textarea(
                attrs={'rows': 3,
                       'placeholder': 'List your skills...'}),
            'qualification': forms.Textarea(
                attrs={'rows': 2,
                       'placeholder': 'Relevant qualifications...'}),
            'location': forms.TextInput(
                attrs={'placeholder': 'e.g., London, UK'}),
        }


# ---------------------------
# JOB MANAGEMENT FORM
# ---------------------------
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter job title'}),
            'description': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Describe the job'}),
        }
