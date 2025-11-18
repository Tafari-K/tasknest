from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, JobForm, ProfileAvatarForm
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


@login_required
def dashboard(request):
    profile = getattr(request.user, 'profile', None)

    # ACTIVE (not deleted)
    active_jobs_qs = Job.objects.filter(
        created_by=request.user,
        is_active=True,
        is_deleted=False
    )

    # COMPLETED (not deleted)
    completed_jobs_qs = Job.objects.filter(
        created_by=request.user,
        is_active=False,
        is_deleted=False
    )

    # DELETED
    deleted_jobs_qs = Job.objects.filter(
        created_by=request.user,
        is_deleted=True
    )

    context = {
        'profile': profile,
        'active_jobs': active_jobs_qs.count(),
        'completed_jobs': completed_jobs_qs.count(),
        'active_jobs_list': active_jobs_qs,
        'completed_jobs_list': completed_jobs_qs,
        'deleted_jobs_list': deleted_jobs_qs,
    }

    return render(request, 'dashboard.html', context)



@login_required
def dashboard_tradesman(request):
    profile = request.user.profile
    form = ProfileAvatarForm(instance=profile)

    active_jobs = profile.user.job_set.filter(status='active').count()
    completed_jobs = profile.user.job_set.filter(status='completed').count()

    return render(request, 'dashboard_tradesman.html', {
        'profile': profile,
        'form': form,
        'active_jobs': active_jobs,
        'completed_jobs': completed_jobs,
    })


@login_required
def dashboard_customer(request):
    profile = request.user.profile
    form = ProfileAvatarForm(instance=profile)

    return render(request, 'dashboard_customer.html', {
        'profile': profile,
        'form': form,
    })


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


@login_required
def restore_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, created_by=request.user)

    job.is_active = True
    job.is_deleted = False
    job.save()

    return redirect('dashboard')


# ============================
# PROFILE / EDIT / SEARCH
# ============================

@login_required
def edit_profile(request):
    return render(request, 'edit_profile.html')


@login_required
def search(request):
    return render(request, 'search.html')

@login_required
def upload_avatar(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    form = ProfileAvatarForm(request.POST, request.FILES, instance=request.user.profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile picture updated successfully.")
    else:
        messages.error(request, "There was a problem updating your profile picture.")

    return redirect(request.POST.get('next') or request.META.get('HTTP_REFERER') or 'dashboard')

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
