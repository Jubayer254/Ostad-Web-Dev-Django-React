from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('experiment/', views.experiment, name='experiment'),
    path('experiment/<person>/', views.experiment, name='experiment'),
    path('experiment/<person>/greetings/<greet>/', views.experiment, name='experiment'),

]
