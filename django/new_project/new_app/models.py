from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=50)
    name_test = models.CharField(max_length=50, default='test')
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    lines = models.IntegerField()

