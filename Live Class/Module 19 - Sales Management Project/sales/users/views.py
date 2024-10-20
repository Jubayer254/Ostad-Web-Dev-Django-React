from django.shortcuts import render, redirect
from .forms import LoginForm, OTPForm
from .models import UserOTP
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
import random
from django.contrib.auth.models import User


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            otp = random.randint(0, 999999)
            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.save()
            request.session['pre_otp_user_id'] = user.id
            print(otp)

            login(request, user)
            return redirect('home')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def otp_verify_view(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            user_id = request.session.get('pre_otp_user_id')
            if user_id is not None:
                user = User.objects.get(id=user_id)
                user_otp = UserOTP.objects.get(user=user)
                if user_otp.otp == otp:
                    user_otp.delete()
                    del request.session['pre_otp_user_id']
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'otp_verify.html', {'form': form, 'error': 'Invalid OTP'})
    form = OTPForm(request.POST)
    return render(request, 'otp_verify.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')