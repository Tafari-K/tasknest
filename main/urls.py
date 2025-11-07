from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),

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
    # path(
    #     'mark-job-complete/<int:job_id>/',
    #     views.mark_job_complete,
    #     name='mark_job_complete'),
    path('add-review/<int:job_id>/', views.add_review, name='add_review'),

    # Profiles
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
