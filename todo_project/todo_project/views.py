from django.shortcuts import render, redirect
from tasks.models import To_do_Model
def home(request):
    return render(request, 'home.html')

def add_task(request):
    if request.method == 'POST':
        Title = request.POST.get('title')
        Descriptions = request.POST.get('descriptions')
        Status = request.POST.get('status')
        Due_Date = request.POST.get('due_date')
        Create_date = request.POST.get('create_date')

        new_task = To_do_Model(
            title=Title,
            description=Descriptions,
            status=Status,
            due_date=Due_Date,
            created_at=Create_date
        )
        new_task.save()

        return redirect('taskList')
    return render(request, 'addTask.html')

def task_list(request):
    tasks = To_do_Model.objects.all()

    context = {
        'tasks': tasks
    }
    return render(request, 'taskList.html', context)

def delete_task(request, task_id):
    task = To_do_Model.objects.get(id=task_id).delete()
    return redirect('taskList')
    # return render(request, 'deleteTask.html', {'task': task})

def update_task(request, task_id):
    task = To_do_Model.objects.get(id=task_id)
    context = {
        'task': task
    }
    if request.method == 'POST':
        task = To_do_Model(
            id = task_id,
            title = request.POST.get('title'),
            description = request.POST.get('descriptions'),
            status = request.POST.get('status'),
            due_date = request.POST.get('due_date'),
            created_at = request.POST.get('create_date')
        )
        task.save()
        return redirect('taskList')
    return render(request, 'updateTask.html', context)