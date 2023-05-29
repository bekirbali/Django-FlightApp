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

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer