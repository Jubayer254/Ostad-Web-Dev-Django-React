from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include("myapp.urls")),
    path('orders/', include("orderapp.urls")),
    path('tasks/', include("todo_app.urls")),
    path('Auth/', include("Auth.urls")),
]
