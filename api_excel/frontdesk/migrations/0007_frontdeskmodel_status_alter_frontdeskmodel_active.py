# Generated by Django 4.1.3 on 2022-12-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0006_frontdeskmodel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontdeskmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='frontdeskmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
