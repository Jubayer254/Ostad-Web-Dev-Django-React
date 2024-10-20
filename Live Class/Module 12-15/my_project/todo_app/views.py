from django.shortcuts import render, redirect
from .models import Task, Book, Author

from django.http import HttpResponse, JsonResponse
from .forms import TaskForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == '1':
        tasks = tasks.filter(completed = True)
    elif completed == '0':
        tasks = tasks.filter(completed = False)
    return render(request, 'task_list.html', {"tasks": tasks})

def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')

    return render(request, 'task_details.html', {"task": task})

def add_task(request):
    _title = 'test'
    _description = 'test'
    _completed = True
    _due_date = "2024-08-28"
    task = Task(title=_title, description=_description, completed=_completed, due_date = _due_date)
    task.save()
    return redirect(task_list)

def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')
    return redirect(task_list)

def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.title = 'Updated'
        task.save()
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')
    return redirect(task_list)

def add_task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # if form.is_valid() and form.cleaned_data["age"] > 150:
        if form.is_valid(): 
            form.save()
            return redirect(task_list)
        else:
            return render(request, 'add_task.html', {"form": form})

    else:
        form = TaskForm()
        return render(request, 'add_task.html', {"form": form})
    
def update_task_form(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        if request.method == 'POST':
            task_form = TaskForm(request.POST, instance=task)
            if task_form.is_valid(): 
                task_form.save()
                return redirect(task_list)
            else:
                return render(request, 'update_task.html', {"form": task_form})
        

        task_form = TaskForm(instance=task)
        return render(request, 'update_task.html', {"form": task_form})
    except Task.DoesNotExist:
        return HttpResponse('Task does not exist')


def task_by_user_id(request, user_id):
    # 1st Method
    # tasks = Task.objects.filter(user_id=user_id).all().values()
    # return JsonResponse({"tasks": list(tasks)})
    # tasks = Task.objects.filter(user_id=user_id)
    # result = []
    # return JsonResponse({"tasks": list(result)})

    # 2nd Method
    # for task in tasks:
    #     result.append({
    #         "user_id": task.user.id,
    #         "user": task.user.first_name + ' ' +task.user.last_name,
    #         "title": task.title,
    #         "description": task.description,
    #         "completed": task.completed,
    #         "created_at": task.created_at,
    #         "due_date": task.due_date
    #     })

    # 3rd Method
    user  = User.objects.get(pk =user_id)
    # tasks = user.task_set.all().values() //If related_name is not declared
    tasks = user.tasks.all().values()
    return JsonResponse({"tasks": list(tasks)})

def all_books(request):
    books = Book.objects.all().values()
    return JsonResponse({"books": list(books)})

def book(request, book_id):
    books = Book.objects.get(pk=book_id)
    # books_details = {
    #     "title": books.title,
    #     "description": books.description,
    #     "publication_date": books.publication_date,
    #     "author": books.author.first_name + ' ' + books.author.last_name # 1 TO MANY
    # }
    books_details = {
        "title": books.title,
        "description": books.description,
        "publication_date": books.publication_date,
        "authors": [f"{author.first_name} {author.last_name}" for author in books.author.all()] # MANY TO MANY
    }

    # return JsonResponse({"books": model_to_dict(books)})
    return JsonResponse({"books": books_details})
    
def author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author_details = {
        "first_name": author.first_name,
        "last_name": author.last_name,
        "bio": author.bio,
        "books": [book.title for book in author.books.all()]
    }
    return JsonResponse({"author": author_details})