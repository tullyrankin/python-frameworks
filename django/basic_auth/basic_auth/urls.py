from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^example1', include('example1.urls')),
]
