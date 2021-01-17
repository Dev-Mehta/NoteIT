from time import sleep
from datetime import date, datetime, time, timedelta
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nts.settings")
django.setup()
from notes.models import Event
from django.contrib.auth.models import User
from django.core.mail import send_mail
from nts import settings
from django.template.loader import get_template
while True:
	today = date.today()
	current_time = datetime.now() + timedelta(minutes=10)
	current_time = time(current_time.hour, current_time.minute)
	events = Event.objects.filter(event_date=today, event_time=current_time)
	print(events)
	for i in range(len(events)):
		event = events[i]
		username = event.user
		username = str(username)
		print(username)
		user = User.objects.get(username=username)
		email = user.email
		if not event.sent_reminder:
			subject = f"Reminder for {event.task_name}"
			context = {
				"user":username,
				"task_name":event.task_name,
				"event_time":event.event_time,
				"event_date":event.event_date,
				"task_details":event.task_detail
			}
			html_message = get_template('html_message.html').render(context)
			send_mail(
				subject,
				html_message,
				settings.EMAIL_HOST_USER,
				[email],
				fail_silently=False,
				html_message=html_message
			)
			print("Sent Mail")
			event.sent_reminder=True
			event.save()
	sleep(1)