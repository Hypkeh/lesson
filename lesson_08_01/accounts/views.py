from django.shortcuts import render
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

# Create your views here.


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('user_profile')
    template_name = 'new_app/post_form.html'


def profile_view(request):
    username = request.user.username
    email = request.user.email
    context = {'username': username, 'email': email}
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
