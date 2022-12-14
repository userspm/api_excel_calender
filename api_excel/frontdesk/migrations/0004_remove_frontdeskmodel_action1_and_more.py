# Generated by Django 4.1.3 on 2022-12-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0003_frontdeskmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontdeskmodel',
            name='Action1',
        ),
        migrations.RemoveField(
            model_name='frontdeskmodel',
            name='Appointment_Time',
        ),
        migrations.RemoveField(
            model_name='frontdeskmodel',
            name='Speciality',
        ),
        migrations.RemoveField(
            model_name='frontdeskmodel',
            name='service_type',
        ),
        migrations.AddField(
            model_name='frontdeskmodel',
            name='Stage',
            field=models.CharField(default='frontdesk', max_length=100),
        ),
    ]
