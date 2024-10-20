from django import forms
from .models import Task
import django.forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']

    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)
    description = forms.CharField(widget=forms.TextInput)
    # title = forms.CharField(widget=forms.TextInput(attrs={'disabled':'true'}))