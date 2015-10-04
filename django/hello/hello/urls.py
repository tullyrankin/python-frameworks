from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'hello.views.index'),
    url(r'^hello/?$', 'hello.views.hello'),
    url(r'^hello/([^/]+)$', 'hello.views.hello_user'),
]
