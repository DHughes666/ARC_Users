# Generated by Django 4.0.5 on 2022-07-03 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AP', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='idd',
            field=models.BigIntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
