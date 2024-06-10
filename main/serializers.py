from rest_framework import serializers
from .models import Post, Valoracion
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ["titulo", "cuerpo", "user", "url"]


class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    fecha_registro = serializers.ReadOnlyField()

    class Meta:
        model = Valoracion
        fields = ["rating", "fecha_registro", "comment", "user", "post", "url"]
