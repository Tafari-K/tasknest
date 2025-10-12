from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('jobs/', views.jobs, name='jobs'),
    path('search/', views.search_jobs, name='search_jobs'),
    path('delete-job/', views.delete_job, name='delete_job'),
]
