from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    JobForm,
    ProfileAvatarForm,
    ProfileForm,
)
from .models import Job, Review
from .utils import is_admin

# ============================
# ADMINISTRATION VIEWS
# ============================


@login_required
def add_job(request):
    if not is_admin(request.user):
        if request.user.profile.role != "tradesman":
            return render(request, "not_authorised.html")


@login_required
def admin_dashboard(request):
    # Only allow admin
    if request.user.profile.role != "admin":
        return render(request, "not_authorised.html")

    context = {
        "total_users": User.objects.count(),
        "total_jobs": Job.objects.count(),
        "total_reviews": Review.objects.count(),
    }
    return render(request, "administration.html", context)


@login_required
def admin_users(request):
    if request.user.profile.role != "admin":
        return render(request, "not_authorised.html")

    return render(request, "admin_users.html")


@login_required
def admin_jobs(request):
    if request.user.profile.role != "admin":
        return render(request, "not_authorised.html")

    return render(request, "admin_jobs.html")


@login_required
def admin_reviews(request):
    if request.user.profile.role != "admin":
        return render(request, "not_authorised.html")

    return render(request, "admin_reviews.html")


# ============================
# AUTHENTICATION VIEWS
# ============================


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'customer':
                return redirect('dashboard_customer')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(
                request, 'registration/login.html',
                {'error': 'Invalid credentials. Please try again.'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ============================
# DASHBOARD VIEWS
# ============================


@login_required
def dashboard(request):
    profile = request.user.profile

    # Jobs
    active_jobs = Job.objects.filter(created_by=request.user, is_active=True)
    completed_jobs = Job.objects.filter(
        created_by=request.user,
        is_active=False,
        is_deleted=False
        )
    deleted_jobs = Job.objects.filter(created_by=request.user, is_deleted=True)

    # REVIEWS
    received_reviews = Review.objects.filter(tradesman=profile)
    customer_reviews = Review.objects.filter(reviewer=profile)

    context = {
        "profile": profile,
        "active_jobs": active_jobs,
        "completed_jobs": completed_jobs,
        "deleted_jobs": deleted_jobs,
        "received_reviews": received_reviews,
        "customer_reviews": customer_reviews,
    }

    # Choose template based on role
    if profile.role == "tradesman":
        return render(request, "dashboard_tradesman.html", context)
    else:
        return render(request, "dashboard_customer.html", context)


@login_required
def complete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, created_by=request.user)

    if request.method == "POST":
        job.is_active = False
        job.save()
        return redirect('dashboard')

    return redirect('dashboard')


@login_required
def restore_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, created_by=request.user)

    job.is_deleted = False
    job.is_active = True
    job.save()

    return redirect('dashboard')


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, created_by=request.user)

    job.is_active = False
    job.is_deleted = True
    job.save()

    return redirect('dashboard')


# ============================
# JOB BOARD VIEWS
# ============================


@login_required
def jobs(request):
    job_list = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': job_list})


@login_required
def add_job(request):
    # Check role from Profile model
    if request.user.profile.role != "tradesman":
        return render(request, "not_authorised.html")

    form = JobForm(request.POST or None)
    if form.is_valid():
        job = form.save(commit=False)
        job.tradesman = request.user
        job.save()
        return redirect("dashboard_tradesman")

    return render(request, "add_job.html", {"form": form})


@login_required
def create_job(request):
    return render(request, 'create_job.html')


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})


# ============================
# PROFILE / EDIT / SEARCH
# ============================

@login_required
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('dashboard')

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def search(request):
    return render(request, 'search.html')


@login_required
def upload_avatar(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    profile = request.user.profile
    form = ProfileAvatarForm(request.POST, request.FILES, instance=profile)

    if form.is_valid():
        form.save()
        messages.success(request, "Profile picture updated successfully.")
    else:
        messages.error(request, "There was an error updating your picture.")

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
# ============================
# REVIEWS
# ============================


@login_required
def add_review(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    reviewer_profile = request.user.profile

    # Determine who is being reviewed
    if reviewer_profile == job.created_by.profile:
        reviewed_profile = job.assigned_to.profile
    else:
        reviewed_profile = job.created_by.profile

    # Prevent double reviewing
    existing_review = Review.objects.filter(
        job=job,
        reviewer=reviewer_profile
    ).first()

    if existing_review:
        messages.warning(request, "You have already reviewed this job.")
        return redirect("dashboard")

    # Handle POST
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment", "")

        Review.objects.create(
            job=job,
            reviewer=reviewer_profile,
            reviewed=reviewed_profile,
            rating=rating,
            comment=comment
        )

        messages.success(request, "Review submitted successfully!")
        return redirect("dashboard")

    return render(request, "add_review.html", {
        "job": job,
        "reviewed": reviewed_profile
    })


# ============================
# HOME + ERROR PAGES
# ============================


def home(request):
    return render(request, 'home.html')


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
