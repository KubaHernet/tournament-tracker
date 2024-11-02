from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("tournaments/", include("tournaments.urls")),
    path("admin/", admin.site.urls)
]
