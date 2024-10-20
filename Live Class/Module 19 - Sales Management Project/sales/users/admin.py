from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)