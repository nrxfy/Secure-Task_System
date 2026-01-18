from django.contrib import admin
from .models import Task, AuditLog, Profile

admin.site.register(Task)
admin.site.register(AuditLog)
admin.site.register(Profile)
