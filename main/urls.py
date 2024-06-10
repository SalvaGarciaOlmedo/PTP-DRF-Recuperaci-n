from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, ValoracionViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename="post")
router.register(r'valoracion', ValoracionViewSet, basename="valoracion")


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
