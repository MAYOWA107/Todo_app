from django.contrib.auth import get_user_model
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import Task

CustomUser = get_user_model()

if 'user' in LogEntry._meta.get_fields():
    LogEntry._meta.get_field('user').remote_field.model = CustomUser

admin.site.register(Task)
admin.site.register(CustomUser)
