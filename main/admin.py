from django.contrib import admin
from .models import Profile, Job, Review


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username',)

# Register your models here.

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Job)
admin.site.register(Review)
