from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-job/', views.add_job, name='add_job'),
    path('remove-job/<int:job_id>/', views.remove_job, name='remove_job'),
    path('mark-complete/<int:job_id>/', views.mark_job_complete, name='mark_job_complete'),
    path('add-review/<int:job_id>/', views.add_review, name='add_review'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
]
