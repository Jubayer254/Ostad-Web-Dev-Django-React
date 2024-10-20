from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    
    # path('task_list/', views.task_list, name="task_list"),
    path('task_list/', views.TaskList.as_view(), name="task_detail"),

    # path('task_detail/<int:pk>/', views.task_detail, name="task_detail"),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view(), name="task_detail"),


]

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename="task")
router.register('books', views.BookViewSet, basename="book")
router.register('authors', views.AuthorViewSet, basename="author")
urlpatterns += router.urls