# Generated by Django 5.0.4 on 2024-05-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_tasks_info_alter_task_is_closed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks_info',
            new_name='TasksInfo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_closed',
        ),
    ]
