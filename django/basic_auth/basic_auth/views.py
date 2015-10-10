from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('Django Index Page')
