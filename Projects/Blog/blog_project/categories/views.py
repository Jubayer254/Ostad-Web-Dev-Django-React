from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('add_categories')  
    else:
        form = CategoryForm()  

    return render(request, 'add_categories.html', {"form": form})