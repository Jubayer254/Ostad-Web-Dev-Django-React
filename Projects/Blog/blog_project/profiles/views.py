from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.
def add_profiles(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('add_posts')  
    else:
        form = ProfileForm()  

    return render(request, 'add_profiles.html', {"form": form})