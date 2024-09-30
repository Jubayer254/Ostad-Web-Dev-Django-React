from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, Django!")

def home(request):
    data = {"name": "Django"}
    return render(request, 'index.html', context=data)

def about(request):
    data = {"name": "Django"}
    return render(request, 'about.html', data)

def contact(request):
    data = {"name": "Django"}
    email = 'jubayerhossen254@gmail.com'
    social_profiles= [
        "Facebook: https://www.facebook.com/jubayer.hossen.254",
        "Instagram: https://www.instagram.com/i.am.jubs/",
        "Linkedin: https://www.linkedin.com/in/jh-cs/"
    ]
    hq = "d"
    return render(request, 'contact.html', {"email": email, "social_profiles" : social_profiles, "hq": hq} | data)

def experiment(request, person = None, greet = None):
    data = {"name": "Django"}
    if person == None:
        person = {"person": "Guest"}
    else:
        person = {"person": person}

    if greet == None:
        greet = {"greet": "Hello"}
    else:
        greet = {"greet": greet}

    return render(request, 'experiment.html', data | person | greet)