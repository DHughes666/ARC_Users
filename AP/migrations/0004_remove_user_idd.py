# Generated by Django 4.0.5 on 2022-07-03 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AP', '0003_user_idd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='idd',
        ),
    ]
