from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

class Appointment(models.Model):
	user = models.EmailField()
	create_date = models.DateTimeField(default=timezone.now)
	appointment_date = models.DateTimeField()

	def __str__(self):
		return self.user

	def get_absolute_url(self):
		return reverse('home')