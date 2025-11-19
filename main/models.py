from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICES = [
        ('tradesman', 'Tradesman'),
        ('customer', 'Customer'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png', blank=True)
    role = models.CharField(
        max_length=15, choices=ROLE_CHOICES, default='customer')
    current_occupation = models.CharField(max_length=50, blank=True)

    location = models.CharField(max_length=50, blank=True)
    skills = models.TextField(blank=True)
    qualification = models.TextField(blank=True)

    jobs_completed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    def get_average_rating(self):
        """Calculate average rating from all reviews received"""
        reviews = self.reviews_received.all()
        if reviews.exists():
            total = sum(review.rating for review in reviews)
            return round(total / reviews.count(), 1)
        return 0

    def get_review_count(self):
        """Get total number of reviews received"""
        return self.reviews_received.count()


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_given')
    tradesman = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_received')

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['job', 'reviewer']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.reviewer.user.username} -> {self.tradesman.user.username} ({self.rating})"



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
