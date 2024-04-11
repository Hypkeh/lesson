from . import views
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register('publishers', views.PublisherViewSet)


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.AuthorList.as_view(), name='drf_author_list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='drf_author_detail'),
    path('', views.spa),
]

urlpatterns += router.urls
