from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
]
