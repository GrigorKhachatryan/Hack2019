from django.shortcuts import render
from event.models import Events, Artists
from django.forms.models import model_to_dict

def hm(request):
    ref = request.GET.get('name') or []
    obj = None
    for event in Events.objects.raw('SELECT * FROM event_events WHERE id == {0}'.format(ref)):
        obj = model_to_dict(event)

    art = None
    for event in Artists.objects.raw('SELECT * FROM event_artists WHERE id == {0}'.format(obj['artist_id'])):
        art = model_to_dict(event)['name']

    obj.update({'name':art})
    print(obj)

    return render(request, 'event_tmp/hello.html', obj)