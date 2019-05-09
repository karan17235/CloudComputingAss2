from django.db import models
from datetime import datetime

# Create your models here.
class AnalyticsUI(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DataTimeField(default=datetime.now, blank=True)
