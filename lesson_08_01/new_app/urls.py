from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('authors/create/', views.AuthorCreate.as_view(), name='create_author'),

    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),

    path('', views.MainPage.as_view(), name='main_page'),

    path('register/', views.UserRegisterView.as_view(), name='registration'),
    path('search/', views.search, name='search_form'),

    path('author_formset/', views.author_formset, name='author_formset'),

    path('atomic/', views.add_record)
]

