# Generated by Django 5.0.4 on 2024-05-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_rename_tasks_info_tasksinfo_remove_task_is_closed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TasksInfo',
        ),
    ]
