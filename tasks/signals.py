from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from .models import AuditLog
from django.contrib.auth.signals import user_logged_out

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(user=user, action="Successful Login", ip_address=request.META.get('REMOTE_ADDR'))

@receiver(user_logged_out) 
def log_user_logout(sender, request, user, **kwargs): AuditLog.objects.create(user=user, action="User Logged Out", ip_address=request.META.get('REMOTE_ADDR'))

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    AuditLog.objects.create(action=f"Failed Login (Username: {credentials.get('username')})", ip_address=request.META.get('REMOTE_ADDR'))