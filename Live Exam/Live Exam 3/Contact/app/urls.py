from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.add_contact, name = 'add_contact'),
    path('contact_detail/<int:pk>', views.contact_detail, name = 'contact_detail'),
    path('edit_contact/<int:pk>', views.edit_contact, name = 'edit_contact'),
    path('delete_contact/<int:pk>', views.delete_contact, name = 'delete_contact'),
    path('home/', views.home, name = 'home')
]