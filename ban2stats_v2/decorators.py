from django.http.response import HttpResponseBadRequest
from django.conf import settings


def token_required(function):
    def inner(request, *args, **kwargs):
        if request.META.get('HTTP_TOKEN'):
            token = settings.BAN2STATS_SERVICE_TOKEN
            if token == request.META.get('HTTP_TOKEN'):
                return function(request, *args, **kwargs)
        return HttpResponseBadRequest("Token is required/mismatched.")
    return inner

