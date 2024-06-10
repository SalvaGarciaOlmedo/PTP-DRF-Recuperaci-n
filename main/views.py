from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post, Valoracion
from .serializers import PostSerializer, ValoracionSerializer
from rest_framework.filters import OrderingFilter


def is_user_valid(model, request, pk):
    if not request.user.is_staff:
        try:
            model.objects.get(user=request.user, pk=pk)
        except model.DoesNotExist:
            return False
    return True


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        if not is_user_valid(Post, request, self.kwargs["pk"]):
            return Response(status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not is_user_valid(Post, request, self.kwargs["pk"]):
            return Response(status=403)
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["fecha_registro"]

    def update(self, request, *args, **kwargs):
        if not is_user_valid(Valoracion, request, self.kwargs["pk"]):
            return Response(status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not is_user_valid(Valoracion, request, self.kwargs["pk"]):
            return Response(status=403)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, fecha_registro=timezone.now())

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

