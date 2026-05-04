from django.urls import path
from .views import latest_update

urlpatterns = [
    path('api/latest-update/', latest_update),
]