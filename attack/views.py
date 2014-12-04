from django.http.response import HttpResponse, HttpResponseBadRequest
from attack.recorder import AttackRecorder
from ban2stats.decorators import token_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from haystack.query import SearchQuerySet


@token_required
def add_attack(request):
    attack_recorder = AttackRecorder()
    try:
        attack_recorder.set_data(**request.REQUEST.copy())
    except ValueError, err:
        print err
        return HttpResponseBadRequest(err)
    try:
        attack_recorder.get_geo_data()
    except ValueError, err:
        print err
        return HttpResponseBadRequest(err)

    attack_recorder.stamp_time()
    attack = attack_recorder.save()
    return HttpResponse('Added attack')


def view_analytics(request):

    attacked_service_search_queryset = SearchQuerySet().facet('attacked_service')
    context = RequestContext(request, {
        'attacked_service_facet': attacked_service_search_queryset.facet_counts()
    })

    country_search_queryset = SearchQuerySet().facet('country_code')
    context.update({
        'country_code_facet': country_search_queryset.facet_counts()
    })

    ip_search_queryset = SearchQuerySet().facet('ip')
    context.update({
        'ip_count': ip_search_queryset.count()
    })
    return render_to_response("analytics_view.html", context)