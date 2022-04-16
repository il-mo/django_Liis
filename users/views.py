from djoser.views import UserViewSet

from api.paginations import PagePagination
from users.models import User
from users.serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    pagination_class = PagePagination

