from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),

    # Jobs
    path('jobs/', views.jobs_view, name='jobs'),
    path('create-job/', views.create_job, name='create_job'),
    path('add-job/', views.create_job, name='add_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('remove-job/<int:job_id>/', views.delete_job, name='remove_job'),
    path('mark-job-complete/<int:job_id>/', views.mark_job_complete, name='mark_job_complete'),
    path('add-review/<int:job_id>/', views.add_review, name='add_review'),

    # Profiles
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]