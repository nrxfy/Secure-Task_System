from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('profile/', views.profile_view, name='profile'),
    path('audit-logs/', views.audit_log_view, name='audit_logs'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

]