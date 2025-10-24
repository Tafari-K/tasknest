from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    ROLE_CHOICES = (
        ('tradesman', 'Tradesman'),
        ('customer', 'Customer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    location = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    avatar_color = models.CharField(max_length=20, default='blue')


    def __str__(self):
        return f"{self.user.username} ({self.role})"

    @property
    def jobs_completed(self):
        return self.job_set.filter(is_completed=True).count()
