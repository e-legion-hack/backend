from django.contrib import admin

# Register your models here.
from employee.models import Employee


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'job_title', 'is_remote')
    list_filter = ('status', 'is_remote', 'is_teamlead', 'is_head_of_departament', 'office', 'departament')
    search_fields = ('first_name', 'last_name', 'email', 'status', 'job_title', 'telegram', 'instagram', 'vkontakte', 'about')
