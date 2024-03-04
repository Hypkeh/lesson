from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

# Create your views here.


class UserLogoutView(LogoutView):
    pass


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  # registration/login.html
    redirect_field_name = 'next'
    authentication_form = AuthenticationForm


def login_view(request):
    default_url = settings.LOGIN_REDIRECT_URL
    next_url = request.GET.get('next', default_url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid username or password',
                                                           'form': AuthenticationForm()})
    else:
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
