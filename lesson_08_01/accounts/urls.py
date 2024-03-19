from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_view'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('permissions/', views.UserPermissions.as_view(), name='user_permissions'),
    path('profile/', views.profile_view, name='user_profile'),
    path('register/', views.SignUpView.as_view(), name='user_register')
]
