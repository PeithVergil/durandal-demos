from django.conf.urls import url

from . import views


urlpatterns = [
    url(regex=r'^$',
        view=views.ListCreateTodoAPIView.as_view(),
        name='create'),

    url(regex=r'^(?P<pk>\d+)/$',
        view=views.RetrieveUpdateDeleteTodoAPIView.as_view(),
        name='retrieve'),
]
