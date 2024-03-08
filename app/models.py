from django.db import models

# Create your models here.
class Messages(models.Model):
    body = models.JSONField()