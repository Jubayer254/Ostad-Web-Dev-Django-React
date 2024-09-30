from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact_Book
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()  
                return redirect('home') 
            except IntegrityError:
                return HttpResponse("Error: The email or phone number already exists. Please use unique values.")
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})

def home(request):
    if request.method == "POST":
        query = request.POST.get('q')
        if query:
            query = query.lower()
            contacts = [contact for contact in Contact_Book.objects.all() if query in contact.first_name.lower() or query in contact.email.lower()]
        else:
            contacts = Contact_Book.objects.all()
        return render(request, 'home.html', {'contacts': contacts})

    contacts = Contact_Book.objects.all() 
    return render(request, 'home.html', {'contacts': contacts})

def contact_detail(request, pk):
    try:
        contact = Contact_Book.objects.get(pk=pk)
        return render(request, 'contact_detail.html', {'contact': contact}) 
    except Contact_Book.DoesNotExist:
            return HttpResponse('Contact does not exist')
    
def edit_contact(request, pk):
    try:
        contact = Contact_Book.objects.get(pk=pk)
        if request.method == 'POST':
            form = ContactForm(request.POST, instance=contact)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('home')
                except IntegrityError:
                    return HttpResponse("Error: The email or phone number already exists.")
        else:
            form = ContactForm(instance=contact)

        return render(request, 'edit_contact.html', {'form': form, 'contact': contact})
    
    except Contact_Book.DoesNotExist:
        return HttpResponse('Contact does not exist')

def delete_contact(request, pk):
    try:
        contact = Contact_Book.objects.get(pk=pk)
        contact.delete()
        return redirect('home')   
    except Contact_Book.DoesNotExist:
        return HttpResponse('Contact does not exist')
