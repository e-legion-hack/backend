from django.contrib import admin

# Register your models here.
from office.models import Office, Departament


@admin.register(Office)
class AdminOffice(admin.ModelAdmin):
    list_display = ('city', 'name', 'address', 'email', 'phone')
    list_filter = ('city', )
    search_fields = ('city', 'name', 'address', 'email', 'phone')


@admin.register(Departament)
class AdminDepartament(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )