from django.contrib import auth
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import UserForm
from .serializers import UserSerializer


User = auth.get_user_model()


class CreateUserView(CreateView):

    model = User

    @property
    def form_class(self):
        return UserForm

    def get_success_url(self):
        """
        Redirect the user to the same registration page.
        """
        return reverse('accounts:create')

    def form_valid(self, form):
        """
        Display a flash message that the account has been created.
        """
        messages.success(self.request, 'Your new account has been created.')

        return super().form_valid(form)


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
