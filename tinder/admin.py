from django.contrib import admin

# Register your models here.
from tinder.models import Activity, LikedActivity


@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
    list_display = ('creator', 'name', 'category', 'place')
    search_fields = ('creator', 'name', 'category', 'place')
    list_filter = ('category', )


@admin.register(LikedActivity)
class AdminLikedActivity(admin.ModelAdmin):
    list_display = ('activity', 'employee')
