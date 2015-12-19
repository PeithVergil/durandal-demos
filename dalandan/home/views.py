from django.views.generic import TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import Todo
from .serializers import TodoSerializer


class IndexView(TemplateView):
    template_name = 'home/index.html'


class ListTodoAPIView(ListAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()


class CreateTodoAPIView(CreateAPIView):

    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()


class DeleteTodoAPIView(DestroyAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()
