from django.db import models

# Create your models here.
class Trend(models.Models):
    month_name = models.CharField(max_length=50)
    month_data = models.IntegerField(max_length=10)

class Profile(models.Model):
    profile_public = models.IntegerField(max_length=20)
    profile_media = models.IntegerField(max_length=20)
    profile_politicians = models.IntegerField(max_length=20)

class Content(models.Models):
    group1_kw = models.IntegerField(max_length=20)
    group2_kw = models.IntegerField(max_length=20)
    group3_kw = models.IntegerField(max_length=20)
