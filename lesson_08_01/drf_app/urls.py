from . import views
from django.urls import path


urlpatterns = [
    path('authors/', views.authors),
    path('books/', views.books),
    path('', views.spa),
]
