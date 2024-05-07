from django.contrib import admin
from .models import Task, TaskStats


# Register your models here.


admin.site.register(Task)
admin.site.register(TaskStats)
