from django.views.generic import TemplateView

from rest_framework.generics import CreateAPIView, UpdateAPIView

from .models import Todo
from .serializers import TodoSerializer


class IndexView(TemplateView):
    template_name = 'home/index.html'


class CreateTodoAPIView(CreateAPIView):

    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):

    serializer_class = TodoSerializer

    @property
    def queryset(self):
        return Todo.objects.all()
