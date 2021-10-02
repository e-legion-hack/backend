from django.contrib import admin

# Register your models here.
from job.models import Task, Project


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('status', 'title', 'created_at', 'finished_at')
    list_filter = ('status', )
    search_fields = ('status', 'title', 'commentary')


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_at', 'end_at')
    list_filter = ('status', )
    search_fields = ('name', 'status')
