from django.conf.urls import url

from . import views


urlpatterns = [
    url(regex=r'^list/$',
        view=views.ListTodoAPIView.as_view(),
        name='list'),

    url(regex=r'^create/$',
        view=views.CreateTodoAPIView.as_view(),
        name='create'),

    url(regex=r'^(?P<pk>\d+)/update/$',
        view=views.UpdateTodoAPIView.as_view(),
        name='update'),

    url(regex=r'^(?P<pk>\d+)/$',
        view=views.DeleteTodoAPIView.as_view(),
        name='delete'),
]
