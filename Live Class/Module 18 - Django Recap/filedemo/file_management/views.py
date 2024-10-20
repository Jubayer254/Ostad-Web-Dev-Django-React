from django.shortcuts import render, redirect
from .models import Documents
from .forms import DocumentForm

# Create your views here.
def file_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload')
        
    form = DocumentForm()
    documents = Documents.objects.all()
    return render(request, 'file_upload.html', {'form': form, 'documents' : documents})