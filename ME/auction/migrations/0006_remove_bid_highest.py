# Generated by Django 3.2.5 on 2022-07-20 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20220719_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='highest',
        ),
    ]