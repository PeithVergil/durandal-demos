from django.conf.urls import include, url


urlpatterns = [
    url(r'^accounts/', include('dalandan.accounts.urls', namespace='accounts')),

    url(r'^', include('dalandan.home.urls', namespace='home')),

    ###################################
    # Register APIs.
    ###################################

    url(r'^api/v1/todos/', include('dalandan.home.apis', namespace='todos_api')),
]
