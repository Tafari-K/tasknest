from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, JobForm
from .models import Job, Profile

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
                {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ============================
# DASHBOARD VIEWS
# ============================

def dashboard(request):
    profile = getattr(request.user, 'profile', None)

    active_jobs = Job.objects.filter(
        created_by=request.user,
        is_active=True).count() if profile else 0
    completed_jobs = Job.objects.filter(
        created_by=request.user,
        is_active=False).count() if profile else 0

    return render(request, 'dashboard.html', {
        'profile': profile,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
    })


# ============================
# JOB VIEWS
# ============================

@login_required
def jobs(request):
    job_list = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': job_list})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, 'Job added successfully!')
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})


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


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard')
    return render(request, 'delete_job.html', {'job': job})


# ============================
# PROFILE / EDIT / SEARCH
# ============================

@login_required
def edit_profile(request):
    return render(request, 'edit_profile.html')


@login_required
def search(request):
    return render(request, 'search.html')


# ============================
# REVIEWS
# ============================

@login_required
def add_review(request):
    return render(request, 'add_review.html')


# ============================
# HOME + ERROR PAGES
# ============================

def home(request):
    return render(request, 'home.html')


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
