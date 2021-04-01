from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import PostView

router = DefaultRouter()
router.register('post', PostView)

urlpatterns = [
    path('', include(router.urls)),
]