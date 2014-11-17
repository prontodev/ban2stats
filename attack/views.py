from django.http.response import HttpResponse, HttpResponseBadRequest
from attack.recorder import AttackRecorder


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