from django.shortcuts import render
from event.models import Events, Artists, Polls, Questions
from django.forms.models import model_to_dict
from django.db import connection
from django.shortcuts import redirect
import requests
from django.http import HttpResponse



def hm(request):
    ref = request.GET.get('name') or []
    obj = None
    for event in Events.objects.raw('SELECT * FROM event_events WHERE id == {0}'.format(ref)):
        obj = model_to_dict(event)

    art = None
    for event in Artists.objects.raw('SELECT * FROM event_artists WHERE id == {0}'.format(obj['artist_id'])):
        art = model_to_dict(event)['name']

    obj.update({'name': art})
    print(obj)
    result = []
    id = []
    for pol in Polls.objects.raw('SELECT * FROM event_polls WHERE event_id_id = {0}'.format(ref)):
        id.append(model_to_dict(pol)['id'])
        result.append(model_to_dict(pol)['name'])
    dict = {}
    dict_id = {}
    dict_count = {}
    second = []
    count = []

    j = 0
    for i in id:
        for question in Questions.objects.raw('SELECT * FROM event_questions WHERE poll_id_id = {0}'.format(i)):
            second.append(model_to_dict(question)['name'])
            count.append(model_to_dict(question)['score'])
        for q in range(len(second)):
            print(count[q], second[q])
            dict_count.update({second[q]: count[q]})
        dict.update({result[j]: second})

        dict_id.update({result[j]: i})
        j += 1
        second = []
    print(dict, dict_id, dict_count, count)
    max = 0
    for i in count:
        if max < i:
            max = i

    response = render(request, 'event_tmp/concertPage.html', {'obj': obj, 'dict': dict, 'dict_id': dict_id,
                                                              'dict_count': dict_count, 'count': count, 'max': max})
    response.set_cookie('ref', ref)
    return response


def add(request):
    event_id = request.COOKIES['ref']
    opros = request.POST.get('opros')
    quest = request.POST.get('quest')
    x = quest.split(',')

    print(event_id)
    print(opros)
    print(quest)
    print(x)

    cursor = connection.cursor()
    cursor.execute("INSERT INTO event_polls(event_id_id, name) VALUES(%s, %s);", [event_id, opros])

    event = []
    for ev in Polls.objects.all().filter(name=opros):
        event.append(model_to_dict(ev))
    print(event[0])
    opros_id = event[0]['id']

    for i in x:
        cursor.execute("INSERT INTO event_questions(poll_id_id, name, score) VALUES(%s, %s, %s);", [opros_id, i, 0])

    return redirect('/event/?name={0}'.format(event_id))


def upgrade(request):
    event_id = request.COOKIES['ref']
    val = request.POST.get('name_name')

    event = []
    for ev in Questions.objects.all().filter(name=val):
        event.append(model_to_dict(ev))
    print(event[0])
    opros_id = event[0]['id']

    print(val, opros_id)

    cursor = connection.cursor()
    cursor.execute("UPDATE event_questions SET score = score + 1 WHERE id = %s", [opros_id])

    return redirect('/event/?name={0}'.format(event_id))


def new_number(request):
    event_id = request.COOKIES['ref']
    number = request.POST.get('number')
    print(number)
    s = str(int(str(number)[-5:])//2*3)
    print(s)


    #number = '+78113112'
    #f = open('contacts.txt', 'a')
    #f.write(number + ',')
    r = requests.get('https://sms.ru/sms/send?api_id=E153FE51-B4E2-7B9E-2EC7-E3DD557D9EA1&to={0}&msg={1}&json=1'.format(str(number), s))
    print(r.json())

    response = render(request, 'event_tmp/form.html')
    response.set_cookie('number', number)
    return response


def check(request):
    event_id = request.COOKIES['ref']
    code = request.POST.get('code')
    number = request.COOKIES['number']
    if str(int(str(number)[-5:])//2*3) == str(code):
        print("УРА")
        f = open('contacts.txt', 'a')
        f.write(number + ',')
    else:
        return HttpResponse("<h3>Неверный код</h3>")

    return redirect('/event/?name={0}'.format(event_id))
