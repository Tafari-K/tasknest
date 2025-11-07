from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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
                return redirect('customer_dashboard')
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
    profile = None
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    return render(request, 'dashboard.html', {'profile': profile})


@login_required
def customer_dashboard(request):
    return render(request, 'dashboard_customer.html')


@login_required
def tradesman_dashboard(request):
    return render(request, 'dashboard_tradesman.html')


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
            job.user = request.user
            job.save()
            return redirect('dashboard')
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
