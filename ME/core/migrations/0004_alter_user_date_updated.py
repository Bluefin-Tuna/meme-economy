# Generated by Django 3.2.5 on 2022-07-08 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220708_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 8, 21, 57, 18, 788779, tzinfo=utc)),
        ),
    ]
