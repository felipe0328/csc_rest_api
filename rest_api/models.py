from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default="pending")
    data = models.JSONField()
    result = models.CharField(max_length=200, null=True)
