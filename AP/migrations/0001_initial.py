# Generated by Django 4.0.5 on 2022-07-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=40)),
                ('last_Name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=90, unique=True)),
            ],
        ),
    ]