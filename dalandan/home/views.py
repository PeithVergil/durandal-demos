from django.views.generic import TemplateView

from rest_framework.generics import CreateAPIView

from .serializers import TodoSerializer


class IndexView(TemplateView):
    template_name = 'home/index.html'


class CreateTodoAPIView(CreateAPIView):

    serializer_class = TodoSerializer
