from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NewTask(models.Model):
	STATUS_CHOICES = (
		(0, "New"),
		(1, "Doing"),
		(2, "Done"),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=30)
	description = models.TextField()
	date_create = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS_CHOICES)

	def __str__(self):
		return self.name

