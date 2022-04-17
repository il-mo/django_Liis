from django.contrib.auth import get_user_model
from rest_framework import viewsets


from api.models import Post
from api.paginations import PagePagination
from api.permissions import IsAdminOrIsAuthorOrReadOnly
from api.serializers import PostSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrIsAuthorOrReadOnly]
    pagination_class = PagePagination

    def get_queryset(self, current_user=None):
        users = User.objects.all()
        if self.request.user in users:
            return Post.objects.all()
        else:
            return Post.objects.filter(visible='for_all')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
