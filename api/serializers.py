from rest_framework import serializers

from api.models import Post
from users.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        fields = (
            'id',
            'author',
            'name',
            'text',
        )
        model = Post
