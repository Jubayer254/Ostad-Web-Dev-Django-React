from django.urls import path
from . import views
urlpatterns = [
    path('v1/signup/', views.registration, name='signup'),
    path('v2/signup/', views.registrationV2, name='signupV2'),
    path('v1/login/', views.login_view, name='login'),
    path('v1/logout/', views.logout_view, name='logout'),
]