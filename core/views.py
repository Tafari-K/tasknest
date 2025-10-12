from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def jobs(request):
    return render(request, 'jobs.html')


def search_jobs(request):
    return render(request, 'search.html')


def delete_job(request):
    return render(request, 'delete_job.html')