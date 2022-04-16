from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet
from users.views import CustomUserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
