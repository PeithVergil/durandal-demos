from django.conf.urls import include, url


urlpatterns = [
    url(r'^accounts/', include('dalandan.accounts.urls', namespace='accounts')),

    url(r'^', include('dalandan.home.urls', namespace='home')),
]