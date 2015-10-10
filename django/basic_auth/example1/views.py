from django.shortcuts import HttpResponse

from .decorators import logged_in_or_basicauth


@logged_in_or_basicauth('Restricted')
def home(request):
    return HttpResponse('Example 1 Index')
