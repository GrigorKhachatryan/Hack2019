from django.shortcuts import render
from event.models import Artists

def hm(request):
    all_artist = Artists.objects.raw('SELECT id, name FROM event_artists')
    print(all_artist)

    return render(request, 'index.html')