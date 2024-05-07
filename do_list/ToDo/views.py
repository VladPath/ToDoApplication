from django.http import HttpResponse
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Task, TaskStats

MAX_TASKS = 10


def earliest_object_delete(x):
    earliest_object = x
    earliest_object.delete()
    return redirect('index')
    
# Create your views here.
def index(request):
    todos = Task.objects.all()
    all_todo_in_work = TaskStats.objects.latest('id').open_tasks
    all_end_todo = TaskStats.objects.latest('id').closed_tasks
    
    if all_todo_in_work > MAX_TASKS:
        earliest_object = Task.objects.earliest('created_at')
        earliest_object.delete()
        latest_object = TaskStats.objects.latest('id')
        latest_object.closed_tasks += 1
        latest_object.open_tasks -= 1
        latest_object.save()
        
    return render(request, 'ToDo/index.html', {'ToDo':todos, 
                                               'title':'Главная страница',
                                               'all_todo_in_work':all_todo_in_work,
                                               'all_end_todo':all_end_todo,
                                               'user': Task.user_id,
                                               })



@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title'] 
    todo = Task(title=title)
    todo.save()
    latest_object = TaskStats.objects.latest('id')
    latest_object.open_tasks += 1
    latest_object.save()
    return redirect('index')

@require_http_methods(['POST'])
@csrf_exempt
def add_five(request):
    for i in range(1,6):
        title = request.POST[str(i)]
        todo = Task(title=title)
        todo.save()
        latest_object = TaskStats.objects.latest('id')
        latest_object.open_tasks += 1
        latest_object.save()
    return redirect('index')


def update(request, todo_id):
    
    todo = Task.objects.get(id=todo_id) 
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    latest_object = TaskStats.objects.latest('id')
    latest_object.closed_tasks += 1
    latest_object.open_tasks -= 1
    latest_object.save()
    
    todo.delete()
    return redirect('index')









