from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

ROLE_CHOICES = [
        ('tradesman', 'Tradesman'),
        ('customer', 'Customer'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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


class Review(models.Model):
    """Model for reviews between customers and tradesmen"""
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='reviews_given')
    reviewed = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='reviews_received')
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
        return (
            f"{self.reviewer.user.username} → "
            f"{self.reviewed.user.username} "
            f"({self.rating})"
        )
