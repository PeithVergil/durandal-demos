from django.conf.urls import url

from . import views


urlpatterns = [
    url(regex=r'^create/$',
        view=views.CreateTodoAPIView.as_view(),
        name='create'),
]