from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(regex=r'^list/$',
        view=views.ListUserView.as_view(),
        name='list'),

    url(regex=r'^new/$',
        view=views.CreateUserView.as_view(),
        name='create'),

    url(regex=r'^me/$',
        view=views.RetrieveUserView.as_view(),
        name='retrieve'),

    ########################################
    # Django Authentication
    ########################################

    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logout.html'}, name='logout'),

    ########################################
    # Django Rest Framework JWT
    ########################################

    url(r'^auth/$', 'rest_framework_jwt.views.obtain_jwt_token', name='auth'),
    url(r'^verify/$', 'rest_framework_jwt.views.verify_jwt_token', name='verify'),
    url(r'^refresh/$', 'rest_framework_jwt.views.refresh_jwt_token', name='refresh'),
]
