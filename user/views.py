from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet 

from .serializer import(
    User, UserSerializer
)

# Create your views here.

class UserCreateView(createModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    permission_classes = [AllowAny]


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer