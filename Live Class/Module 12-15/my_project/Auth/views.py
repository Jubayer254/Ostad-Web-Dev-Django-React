from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomSignUPForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/Auth/v1/login/")
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)

def registrationV2(request):   
    if request.method == 'POST':
        form = CustomSignUPForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/Auth/v1/login/")
    else:
        form = CustomSignUPForm()
    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # SESSION
            request.session['name'] = 'jubayer'
            name = request.session.get('name')

            login(request, user)
            return redirect("/tasks/")
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect("/Auth/v1/login/")
