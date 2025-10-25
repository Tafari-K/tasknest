from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Model for reviews between customers and tradesmen"""
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_given')
    reviewed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    comment = models.TextField(blank=True, help_text="Optional feedback")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure one review per job per reviewer
        unique_together = ['job', 'reviewer']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.reviewer.user.username} → {self.reviewed.user.username} ({self.rating}★)"