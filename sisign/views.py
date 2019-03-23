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
    response = redirect('/event/?name=' + str(obj))
    response.set_cookie('email', email)
    response.set_cookie('ticket', ticket)
    response.delete_cookie('login')
    if obj == None:
        return render(request, 'error.html')
    return response

def artist(request):


    login = '"' + request.POST.get('email') + '"'
    password = request.POST.get('password')
    obj = None
    for art in Artists.objects.raw('SELECT * FROM event_artists WHERE log =={0} and pas == {1}'.format(login,password)):
        obj = model_to_dict(art)
        id = obj['id']
    response = redirect('../artist/?name='+ str(id))
    response.set_cookie('login', login)
    response.delete_cookie('email')
    if obj == None:
        return render(request, 'error.html')
    return response


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
    if 'login' not in request.COOKIES:
        cook_login = False
    else:
        cook_login = True
    if 'email' not in request.COOKIES:
        cook_email = False
    else:
        cook_email = True
    result = []
    for ev in Events.objects.all().filter(artist_id = art_id):
        result.append(model_to_dict(ev)['id'])
    print(result)
    result_sum = [0]* (len(result))
    j = 0
    for i in result:

        for it in Fans.objects.all().filter(event_id = i):
            result_sum[j] += 1
            print(model_to_dict(it))
        j += 1
    stat = int(sum(result_sum)/len(result_sum))
    return render(request, 'artist.html', {'art': obj, 'pol':event, 'cook_login': cook_login, 'cook_email': cook_email, 'stat': stat})


def feedback(request):
    f = open('text.txt', 'w')
    f.write('name: ' + request.POST.get('name') + '\n')
    f.write('phone: ' + request.POST.get('phone') + '\n')
    f.write('email: ' + request.POST.get('email') + '\n')
    f.write('text: ' +request.POST.get('text') + '\n')
    return redirect('/')

def exit(request):
    response = redirect('/')
    response.delete_cookie('email')
    return response

def chat(request):
    if 'login' not in request.COOKIES:
        bool = False
    else:
        bool = True

    return render(request, "chat.html", {'bool': bool})


# Create your views here.
