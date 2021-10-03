from django.urls import path, include

urlpatterns = [
    path('employee/', include('api.employee.urls')),
    path('e-tinder/', include('api.tinder.urls')),
    path('task/', include('api.tasks.urls')),
]
