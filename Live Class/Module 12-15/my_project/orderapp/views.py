from django.shortcuts import render

# Create your views here.
def order(request):
    data = {"name" : "Django"}
    return render(request, 'order.html', data)
    
