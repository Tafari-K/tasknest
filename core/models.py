from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
