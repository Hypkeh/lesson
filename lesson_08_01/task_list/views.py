from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Task
from django.contrib import messages

class TaskList(ListView):
    model = Task
    paginate_by = 1
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Все авторы')
        return super().dispatch(request, *args, **kwargs)


def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks ,1,  orphans=1)  
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "new_app/task_list.html",context)


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    form_class = '' 
    success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')

class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')

class TaskDetail(DetailView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    pass






































