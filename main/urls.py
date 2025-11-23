from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),

    # Administration
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/admin/users/", views.admin_users, name="admin_users"),
    path("dashboard/admin/jobs/", views.admin_jobs, name="admin_jobs"),
    path("dashboard/admin/reviews/", views.admin_reviews, name="admin_reviews"),


    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),

    # Jobs
    path('jobs/', views.jobs, name='jobs'),
    path('create-job/', views.create_job, name='create_job'),
    path('add-job/', views.add_job, name='add_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path(
        'remove-job/<int:job_id>/',
        views.delete_job,
        name='remove_job'),
    path(
        'mark-job-complete/<int:job_id>/',
        views.complete_job,
        name='complete_job'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path(
        'restore-job/<int:job_id>/',
        views.restore_job,
        name='restore_job'),
    path('add-review/<int:job_id>/', views.add_review, name='add_review'),

    # Profiles
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/avatar/', views.upload_avatar, name='upload_avatar'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
