from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_view'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('permissions/', views.UserPermissions.as_view(), name='user_permissions'),
    path('profile/', views.profile_view, name='user_profile'),
    path('register/', views.register, name='user_register'),
    path('upload_file/', views.add_file, name='upload_file'),
    path('upload_photo/', views.add_photo, name='upload_photo'),
    path('delete_photo/<int:pk>', views.delete_photo, name='delete_photo'),
    path('activate/<str:signed_username>/', views.activate, name='user_activate')
]
