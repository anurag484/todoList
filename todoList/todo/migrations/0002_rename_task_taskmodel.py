# Generated by Django 4.1.7 on 2023-10-17 16:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='task',
            new_name='taskModel',
        ),
    ]