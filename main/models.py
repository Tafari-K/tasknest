from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ('tradesman', 'Tradesman'),
        ('customer', 'Customer'),
    )

    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    current_occupation = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    qualification = models.TextField(blank=True)
    jobs_completed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Job(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
