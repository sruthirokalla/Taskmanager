# taskmanager/urls.py
from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # This includes the URLs from the 'tasks' app
]
