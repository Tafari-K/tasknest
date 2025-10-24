from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from .forms import ProfileForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


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


@login_required
def dashboard(request):
    profile = request.user.profile

    active_jobs = profile.job_set.filter(is_completed=False)
    completed_jobs = profile.job_set.filter(is_completed=True)

    context = {
        'profile': profile,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
        'active_jobs_count': active_jobs.count(),
        'completed_jobs_count': completed_jobs.count(),
        'reviews': [],  # Placeholder for reviews
    }

    if profile.role == 'tradesman':
        return render(request, 'dashboard_tradesman.html', context)
    elif profile.role == 'customer':
        return render(request, 'dashboard_customer.html', context)
    else:
        return render(request, 'dashboard.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.profile = request.user.profile
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})


@login_required
def remove_job(request, job_id):
    job = Job.objects.get(id=job_id, profile=request.user.profile)
    job.delete()
    return redirect('dashboard')


def home(request):
    return render(request, 'home.html')


def jobs_view(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})


def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs')
    return render(request, 'delete_job.html', {'job': job})


@login_required
def mark_job_complete(request, job_id):
    job = Job.objects.get(id=job_id, profile=request.user.profile)
    job.is_completed = True
    job.save()
    return redirect('dashboard')

