from django.db import models
from django.contrib.auth.models import User


CATEGORIES = (
	(0, "None"),
	(1, "Study"),
	(2, "Work"),
	(3, "Gym"),
	(4, "Business"),
	(5, "Holiday")
)
class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task_name = models.CharField(max_length=140)
	task_detail = models.CharField(max_length=140)
	event_date = models.DateField()
	event_time = models.TimeField()
	created_on = models.DateTimeField(auto_now_add=True)
	sent_reminder = models.BooleanField(default=False)
	category = models.IntegerField(choices=CATEGORIES,default=CATEGORIES[0])