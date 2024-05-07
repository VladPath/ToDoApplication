from django.db import models

# Create your models here.


class TaskStats(models.Model):
    open_tasks = models.IntegerField(default=0)
    closed_tasks = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Статус задания'
        verbose_name_plural = 'Статус заданий'
        
    

    


class Task(models.Model):
    user_id = models.IntegerField(default=1)
    title = models.CharField('Название задания', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        
    def __str__(self):
        return self.title
        