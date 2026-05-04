from django.db import models

class AppUpdate(models.Model):
    version_code = models.IntegerField()
    version_name = models.CharField(max_length=50)
    apk_file = models.FileField(upload_to='apk/')
    force_update = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Version {self.version_name}"