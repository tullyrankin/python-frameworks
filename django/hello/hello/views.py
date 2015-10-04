from django.http import HttpResponse


def index(request):
    return HttpResponse('Django Index Page')


def hello(request):
    return HttpResponse('Hello World!')


def hello_user(request, user):
    return HttpResponse('Hello {0}!'.format(user))
