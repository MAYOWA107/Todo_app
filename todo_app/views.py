from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMessage
from Todo_list.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetView

from .forms import CustomUserCreationForm


class TaskLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')    
    


class SignupPage(FormView):
    template_name = 'accounts/signup.html'
    redirect_authenticated_user = True
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(SignupPage, self).get(*args, **kwargs)           
    

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 6
    template_name = 'todo_list.html'


    def get_queryset(self):
            # Filter tasks based on the currently logged-in user
        queryset = Task.objects.filter(user=self.request.user)
        return Task.objects.order_by('create')
        
        # Apply search filter if provided in the query parameters
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            queryset = queryset.filter(title__startswith=search_input)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        context['search_input'] = search_input
        return context
    

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo_detail.html'
    context_object_name = 'detail'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo_form.html'
    fields = ['title', 'description', 'complete',]
    success_url = reverse_lazy('task')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ['title', 'description',]
    success_url = reverse_lazy('task')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'delete.html'

class My_Password_Change_Views(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = 'password_change/done'

class My_Password_Change_Done_View(PasswordChangeDoneView):
    template_name= 'accounts/password_change_done.html'
    

class Password_Reset_View(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_done')








