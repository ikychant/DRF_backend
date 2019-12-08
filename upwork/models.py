from django.db import models

class Job(models.Model):
    job_url = models.fields.CharField(max_length=255)
