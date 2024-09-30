from django.shortcuts import render
from .forms import SearchForm, AddToDoForm
from .models import todo

# Create your views here.


# def todos(request):

#     # http://127.0.0.1:8000/todo/?name=Jubayer&age=10
#     print(request.GET)
#     name = request.GET.get('name')
#     age = request.GET.get('age')
#     print(name)

#     return render(request, 'todoapp/todos.html', {"name": name, "age":age, "todos_test_data": todos_test_data})


def todos(request):

    todos_test_data = [
        {"title": "Buy groceries", "completed": False},
        {"title": "Complete Python assignment", "completed": True},
        {"title": "Call the bank", "completed": False},
        {"title": "Walk the dog", "completed": True},
        {"title": "Read a book", "completed": False},
        {"title": "Prepare for the meeting", "completed": True},
        {"title": "Send email updates", "completed": False},
        {"title": "Workout", "completed": True},
        {"title": "Plan weekend trip", "completed": False},
        {"title": "Clean the house", "completed": True}
    ]

    # search_form = SearchForm(request.GET)
    search_form = SearchForm(request.POST)

    query = None
    # query = request.GET.get('query')

    if request.method == "POST":
        if search_form.is_valid():
            query = search_form.cleaned_data["query"]

        if query:
            todos_test_data = [
                todo for todo in todos_test_data if query.lower() in todo['title'].lower()
            ]

    return render(request, 'todoapp/todos.html', {"todos_test_data": todos_test_data, "search_form": search_form})


def add_todo(request):
    if request.method == "POST":
        add_todo_form = AddToDoForm(request.POST)
        if add_todo_form.is_valid():
            add_todo_form.save()

    add_todo_form = AddToDoForm()
    todos = todo.objects.all()
   
    return render(request, 'todoapp/add_todo.html', {"add_todo_form": add_todo_form, "todos": todos})