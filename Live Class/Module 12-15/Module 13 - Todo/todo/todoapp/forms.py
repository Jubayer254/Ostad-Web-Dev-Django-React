from django import forms
from .models import todo

# Create your models here.
class SearchForm(forms.Form):
    query = forms.CharField(
        widget = forms.TextInput(attrs={"class": "form-control"}),
    )

class AddToDoForm(forms.ModelForm):
    class Meta:
        model = todo
        # fields = ["title", "completed"]
        fields = "__all__"