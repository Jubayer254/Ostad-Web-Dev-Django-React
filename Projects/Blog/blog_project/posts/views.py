from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from . import forms

# Create your views here.
def add_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('add_posts')  
    else:
        form = PostForm()  

    return render(request, 'add_posts.html', {"form": form})

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = forms.PostForm(instance=post)

    if request.method == "POST":
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit_post.html', {"form": form})

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/')