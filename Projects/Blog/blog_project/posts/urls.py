from django.urls import path
from . import views

urlpatterns = [
    path('add_posts/', views.add_posts, name='add_posts'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
]
