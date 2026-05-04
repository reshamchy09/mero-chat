from django.contrib import admin
from .models import AppUpdate

@admin.register(AppUpdate)
class AppUpdateAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_code', 'force_update', 'uploaded_at')