from django.contrib import admin
from django.urls import path
from forex_app.views import test_response

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", test_response)
]