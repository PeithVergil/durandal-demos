from django.conf.urls import url

from . import views


########################################
# Django Rest Framework JWT
########################################

urlpatterns = [
    url(r'^auth/$', 'rest_framework_jwt.views.obtain_jwt_token', name='auth'),
    url(r'^verify/$', 'rest_framework_jwt.views.verify_jwt_token', name='verify'),
    url(r'^refresh/$', 'rest_framework_jwt.views.refresh_jwt_token', name='refresh'),
]

urlpatterns += [
    url(regex=r'^list/$',
        view=views.ListUserView.as_view(),
        name='list'),

    url(regex=r'^new/$',
        view=views.CreateUserView.as_view(),
        name='create'),
    
    url(regex=r'^me/$',
        view=views.RetrieveUserView.as_view(),
        name='retrieve'),
]