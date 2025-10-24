from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import CustomUserCreationForm, ProfileForm, JobForm

# ===============================
# AUTHENTICATION VIEWS
# ===============================

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = user.profile

            if profile.role == 'customer':
                return redirect('customer_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# ===============================
# PROFILE MANAGEMENT
# ===============================

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


# ===============================
# DASHBOARD VIEWS
# ===============================

@login_required
def dashboard(request):
    """Decides which dashboard to render based on user role."""
    profile = request.user.profile
    if profile.role == 'tradesman':
        active_jobs = profile.job_set.filter(is_completed=False)
        completed_jobs = profile.job_set.filter(is_completed=True)
        context = {
            'profile': profile,
            'active_jobs': active_jobs,
            'completed_jobs': completed_jobs,
            'active_jobs_count': active_jobs.count(),
            'completed_jobs_count': completed_jobs.count(),
            'reviews': [],
        }
        return render(request, 'dashboard_tradesman.html', context)
    elif profile.role == 'customer':
        return redirect('customer_dashboard')
    else:
        return render(request, 'dashboard.html', {'profile': profile})


@login_required
def customer_dashboard(request):
    """Dashboard view for customers."""
    profile = request.user.profile
    posted_jobs = profile.job_set.all()
    completed_jobs = posted_jobs.filter(is_completed=True)
    pending_jobs = posted_jobs.filter(is_completed=False)

    context = {
        'profile': profile,
        'posted_jobs': posted_jobs,
        'completed_jobs': completed_jobs,
        'posted_jobs_count': posted_jobs.count(),
        'completed_jobs_count': completed_jobs.count(),
        'pending_jobs_count': pending_jobs.count(),
    }

    return render(request, 'dashboard_customer.html', context)


# ===============================
# JOB MANAGEMENT
# ===============================
def jobs_view(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.profile = request.user.profile
            job.save()
            return redirect('customer_dashboard')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, profile=request.user.profile)
    if request.method == 'POST':
        job.delete()
        return redirect('customer_dashboard')
    return render(request, 'delete_job.html', {'job': job})


@login_required
def mark_job_complete(request, job_id):
    job = get_object_or_404(Job, id=job_id, profile=request.user.profile)
    job.is_completed = True
    job.save()
    return redirect('dashboard')


# ===============================
# STATIC/HOME VIEWS
# ===============================

def home(request):
    return render(request, 'home.html')
