from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from . import forms
from .models import UserFile, UserPhoto

# Create your views here.


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('user_profile')
    template_name = 'new_app/post_form.html'


def profile_view(request):
    username = request.user.username
    email = request.user.email
    user = request.user
    photos = user.userphoto_set.all()
    context = {'username': username, 'email': email, 'photos': photos}
    return render(request, 'accounts/profile.html', context)


class UserPermissions(TemplateView):
    template_name = 'accounts/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.request.user.get_all_permissions()
        return context


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/'  # reverse('password_change_done') - default


class UserLogoutView(LogoutView):
    pass


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  # registration/login.html


def login_view(request):
    default_url = settings.LOGIN_REDIRECT_URL
    next_url = request.GET.get('next', default_url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid username or password',
                                                           'form': AuthenticationForm()})
    else:
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})


def add_file(request):
    if request.method == 'POST':
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            new_file = form.save(commit=False)
            new_file.user_id = user
            new_file.save()
            return redirect('main_page')
    else:
        form = forms.FileForm()
    context = {'form': form}
    return render(request, 'accounts/file_form.html', context)


def add_photo(request):
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            new_file = form.save(commit=False)
            new_file.user_id = user
            new_file.save()
            return redirect('main_page')
    else:
        form = forms.PhotoForm()
    context = {'form': form}
    return render(request, 'accounts/file_form.html', context)


def delete_photo(request, pk):
    if request.method == 'POST':
        img = UserPhoto.objects.get(pk=pk)
        img.image.delete()
        img.delete()
        return redirect('user_profile')

# django-cleanup - очистка от файлов без записи в БД