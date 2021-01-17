# Generated by Django 2.2.6 on 2021-01-17 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=140)),
                ('task_detail', models.CharField(max_length=140)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sent_reminder', models.BooleanField(default=False)),
                ('category', models.IntegerField(choices=[(0, 'None'), (1, 'Study'), (2, 'Work'), (3, 'Gym'), (4, 'Business'), (5, 'Holiday')], default=(0, 'None'))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]