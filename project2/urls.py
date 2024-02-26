from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('secretadmin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('django_prometheus.urls')),
]