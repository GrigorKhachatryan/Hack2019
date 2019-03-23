from django.shortcuts import render, redirect
from event.models import Fans, Artists, Events
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'startPage.html')

def check(request):
    email = '"' + request.POST.get('email') + '"'
    ticket = request.POST.get('ticket')
    obj = None
    for tick in Fans.objects.raw('SELECT * FROM event_fans WHERE email == {0}  and ticket == {1}'.format(email, ticket)):
        obj = model_to_dict(tick)['event_id']
        print(obj)
    if obj == None:
        return render(request, 'error.html')
    return redirect('/event/?name=' + str(obj))

def artist(request):


    login = '"' + request.POST.get('email') + '"'
    password = request.POST.get('password')
    obj = None
    for art in Artists.objects.raw('SELECT * FROM event_artists WHERE log =={0} and pas == {1}'.format(login,password)):
        obj = model_to_dict(art)
        id = obj['id']
    if obj == None:
        return render(request, 'error.html')
    return redirect('../artist/?name='+ str(id))


def artist_prof(request):
    art_id= request.GET.get('name') or []

    for art in Artists.objects.raw('SELECT * FROM event_artists WHERE id =={0}'.format(art_id)):
        obj = model_to_dict(art)

    event = []
    # for ev in Events.objects.raw('SELECT * FROM event_events WHERE artist_id != 2'):
    #     event = model_to_dict(ev)
    for ev in Events.objects.all().filter(artist_id = art_id):
        event.append(model_to_dict(ev))
    print(event,event[0]['id'])
    res = []
    for i in range(len(event)):
        event[i].update({'ref':"/event/?name="+ str(event[i]['id'])})
    print(event)

    return render(request, 'artist.html', {'art': obj, 'pol':event})


# Create your views here.
