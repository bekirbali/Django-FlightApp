from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet 

from .serializer import(
    User, UserSerializer
)

# Create your views here.

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer