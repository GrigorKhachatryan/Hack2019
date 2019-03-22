from django.shortcuts import render
from event.models import Artists


def check(request):
    all_artist = Artists.objects.all()
    print(all_artist)

    return render(request, 'index.html')

def artist(request):

    return render(request, 'index.html')




# Create your views here.
