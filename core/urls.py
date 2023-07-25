from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/users/", include(("api.routers", "api"), namespace="api")),
    path('admin/', admin.site.urls),
]
