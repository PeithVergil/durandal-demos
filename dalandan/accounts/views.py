from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


User = get_user_model()


# class ListCreateUserViewSet(ModelViewSet):
    
#     @property
#     def queryset(self):
#         return User.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return CreateUserSerializer
#         else:
#             return UserSerializer


class ListUserView(ListAPIView):

    serializer_class = UserSerializer
    
    @property
    def queryset(self):
        return User.objects.all()


class CreateUserView(CreateAPIView):
    
    serializer_class = UserSerializer

    @property
    def queryset(self):
        return User.objects.all()


class RetrieveUserView(RetrieveAPIView):
    
    serializer_class = UserSerializer
    
    permission_classes = (
        IsAuthenticated,
    )

    def get_object(self):
        return self.request.user