from django import forms
from .models import Contact_Book

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Book
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']