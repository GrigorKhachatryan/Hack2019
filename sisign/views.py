from django.shortcuts import render, redirect
from event.models import Fans
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'startPage.html')

def check(request):
    email = request.POST.get('email')
    ticket = request.POST.get('ticket')
    print(email,ticket)
    email = '"'+ email +'"'

    obj = None
    for tick in Fans.objects.raw('SELECT * FROM event_fans WHERE email == {0}  and ticket == {1}'.format(email, ticket)):
        obj = model_to_dict(tick)['event_id']
        print(obj)
    return redirect('/event/?name=' + str(obj))

def artist(request):

    return render(request, 'startPage.html')




# Create your views here.
