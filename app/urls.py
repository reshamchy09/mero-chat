from django.urls import path
from .views import app_update_list, latest_update

urlpatterns = [
    path('api/latest-update/', latest_update),
        path('', app_update_list, name='app_list'),
]