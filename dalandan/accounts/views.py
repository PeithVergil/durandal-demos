from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import UserForm
from .serializers import UserSerializer


User = get_user_model()


class CreateUserView(CreateView):

    model = User

    @property
    def form_class(self):
        return UserForm


class ListUserView(ListAPIView):

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
