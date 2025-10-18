from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.contrib.auth.forms import UserCreationForm


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
