from django.views.generic import TemplateView

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)

from .models import Todo
from .serializers import TodoSerializer


class IndexView(TemplateView):
    template_name = 'home/index.html'


class ListCreateTodoAPIView(ListCreateAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()


class RetrieveUpdateDeleteTodoAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()
