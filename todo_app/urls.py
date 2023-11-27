from django.urls import path
from .views import (TaskListView, TaskDetailView, TaskCreateView,
                     TaskUpdateView, TaskDeleteView, TaskLoginView,
                     SignupPage, My_Password_Change_Done_View, My_Password_Change_Views, Password_Reset_View)

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', SignupPage.as_view(), name='signup'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('login', TaskLoginView.as_view(), name='login'),
    path('', TaskListView.as_view(), name='task'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='detail'),
    path('create', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('password_change', My_Password_Change_Views.as_view(), name='password_change'),
    path('password_change/done', My_Password_Change_Done_View.as_view(), name='password_change_done'),

    #Password reset functionality
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
