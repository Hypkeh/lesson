from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_view'),
    path('tasks/create/', views.TaskCreate.as_view(), name="task_create"),
    path('tasks/delete/<int:pk>/', views.DeleteView.as_view(), name='task_delete'),
    path('tasks/update/<int:pk>/', views.UpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>', views.DetailView.as_view(), name='task_detail'),
    path('tasks/', views.ListView.as_view(), name='task_list'),
]