# Generated by Django 4.1.3 on 2022-12-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0004_remove_frontdeskmodel_action1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelupload',
            name='DOA',
            field=models.CharField(default='null', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frontdeskmodel',
            name='DOA',
            field=models.CharField(default='null', max_length=60),
            preserve_default=False,
        ),
    ]
