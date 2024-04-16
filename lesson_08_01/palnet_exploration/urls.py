from rest_framework.routers import DefaultRouter
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='Space API',
        default_version='1'
    ),
    public=True
)

router = DefaultRouter()
router.register('planets', views.PlanetViewSet, basename='planets')
router.register('explorers', views.ExplorerViewSet, basename='explorers')

urlpatterns = [
    path('docs', schema_view.with_ui('swagger'))
]

urlpatterns += router.urls
